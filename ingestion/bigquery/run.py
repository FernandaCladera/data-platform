from config.config import BIGQUERY_TABLES
from ingestion.bigquery.extract import get_bigquery_client, extract_table
from ingestion.bigquery.load import load_table


client = get_bigquery_client()

for table in BIGQUERY_TABLES:
    print(f"Loading {table}...")
    rows = extract_table(client, table)
    load_table(rows, table)

    print(f"{table} loaded.")