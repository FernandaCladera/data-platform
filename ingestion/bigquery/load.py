import os
import snowflake.connector
from dotenv import load_dotenv

from config.config import SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER,SNOWFLAKE_DATABASE,SNOWFLAKE_BRONZE_SCHEMA,SNOWFLAKE_WAREHOUSE,SNOWFLAKE_ROLE


load_dotenv()

def get_snowflake_connection():
    password = os.getenv("SNOWFLAKE_PASSWORD")
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=password,
        account=SNOWFLAKE_ACCOUNT,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_BRONZE_SCHEMA,
        warehouse=SNOWFLAKE_WAREHOUSE,
        role=SNOWFLAKE_ROLE
    )

def load_table(rows, table_name):
    connection = get_snowflake_connection()
    cursor = connection.cursor()
    try:
        rows = list(rows)
        if not rows:
            return
        columns = list(rows[0].keys())
        placeholders = ", ".join(["%s"]* len(columns))
        column_names = ", ".join(columns)

        query=f"""
            INSERT INTO {table_name} ({column_names})
            VALUES ({placeholders})
        """
        data=[tuple(row[column] for column in columns) for row in rows]
        cursor.executemany(query, data)
        connection.commit()

    finally:
        cursor.close()
        connection.close()