import os
import tempfile
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv

from config.config import SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_DATABASE, SNOWFLAKE_BRONZE_SCHEMA,SNOWFLAKE_WAREHOUSE,SNOWFLAKE_ROLE

load_dotenv()


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=SNOWFLAKE_ACCOUNT,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_BRONZE_SCHEMA,
        warehouse=SNOWFLAKE_WAREHOUSE,
        role=SNOWFLAKE_ROLE,
    )


def load_table(rows, table_name):
    rows = list(rows)

    if not rows:
        return

    dataframe = pd.DataFrame(
        [dict(row.items()) for row in rows]
    )

    # Convert special BigQuery objects to strings
    for column in dataframe.columns:
        if dataframe[column].dtype == "object":
            dataframe[column] = dataframe[column].apply(
                lambda value: value.to_wkt()
                if hasattr(value, "to_wkt")
                else value
            )

    connection = get_snowflake_connection()
    cursor = connection.cursor()
    stage_name = f"{table_name}_stage"

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            parquet_path = os.path.join(
                temp_dir,
                f"{table_name}.parquet",
            )

            dataframe.to_parquet(
                parquet_path,
                index=False,
            )

            cursor.execute(
                f"""
                CREATE TEMP STAGE {stage_name}
                FILE_FORMAT = (TYPE = PARQUET)
                """
            )

            cursor.execute(
                f"""
                PUT 'file://{parquet_path}'
                @{stage_name}
                AUTO_COMPRESS = FALSE
                OVERWRITE = TRUE
                """
            )

            columns = list(dataframe.columns)

            target_columns = ", ".join(
                f'"{column.upper()}"'
                for column in columns
            )

            select_columns = ", ".join(
                (
                    f"TO_GEOGRAPHY($1:\"{column}\"::STRING)"
                    if column.endswith ("_geom")
                    else f'$1:"{column}"'
                )
                for column in columns
            )

            cursor.execute(
                f"""
                COPY INTO {table_name} ({target_columns})
                FROM (
                    SELECT {select_columns}
                    FROM @{stage_name}
                )
                FILE_FORMAT = (TYPE = PARQUET)
                ON_ERROR = 'ABORT_STATEMENT'
                """
            )

            connection.commit()

    finally:
        cursor.close()
        connection.close()