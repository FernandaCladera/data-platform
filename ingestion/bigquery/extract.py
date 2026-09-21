from google.cloud import bigquery
from config.config import GCP_PROJECT_ID, BIGQUERY_SOURCE_PROJECT, BIGQUERY_DATASET


def get_bigquery_client():
    return bigquery.Client(project=GCP_PROJECT_ID)

def extract_orders(client):
    query=f"""
        SELECT * FROM `{BIGQUERY_SOURCE_PROJECT}.{BIGQUERY_DATASET}.orders`
        LIMIT 100
        """
    query_job = client.query(query)
    return query_job.result()


if __name__ == "__main__":
    client = get_bigquery_client()
    rows=extract_orders(client)
    for row in rows:
        print(dict(row))