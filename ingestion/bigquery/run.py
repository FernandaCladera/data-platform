from ingestion.bigquery.extract import get_bigquery_client, extract_table
from ingestion.bigquery.load import load_table


def ingest_table(table):
    client = get_bigquery_client()
    rows = extract_table(client, table)
    load_table(rows, table)