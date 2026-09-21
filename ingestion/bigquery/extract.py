from google.cloud import bigquery
from config.config import GCP_PROJECT_ID, BIGQUERY_SOURCE_PROJECT, BIGQUERY_DATASET


def get_bigquery_client():
    return bigquery.Client(project=GCP_PROJECT_ID)

def extract_table(client, table_name,start_date=None):
    table = f"{BIGQUERY_SOURCE_PROJECT}.{BIGQUERY_DATASET}.{table_name}"
    if start_date is None:
        query = f"""
                SELECT * FROM `{table}`
                """
        return client.query(query).result()
    query = f"""
            SELECT * FROM `{table}`
            WHERE create_at >= @start_date"""

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("start_date", "TIMESTAMP", start_date)
        ]
    )
    return client.query(query, job_config=job_config).result()