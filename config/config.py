import os
# BigQuery Configuration

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BIGQUERY_SOURCE_PROJECT= "bigquery-public-data"
BIGQUERY_DATASET= "thelook_ecommerce"

BIGQUERY_TABLES = [
    "distribution_centers",
    "inventory_items",
    "order_items",
    "products",
    "users"
]

# Snowflake Configuration
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_DATABASE = "DB_ERP"
SNOWFLAKE_WAREHOUSE = "DEV_WH"
SNOWFLAKE_ROLE = "role_dev"
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_BRONZE_SCHEMA = "BRONZE"
SNOWFLAKE_SILVER_SCHEMA = "SILVER"
SNOWFLAKE_GOLD_SCHEMA = "GOLD"


# Others configs
BATCH_SIZE = 5000