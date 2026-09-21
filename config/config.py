# BigQuery Configuration

GCP_PROJECT_ID = "lateral-client-509315-s1"

BIGQUERY_SOURCE_PROJECT= "bigquery-public-data"
BIGQUERY_DATASET= "thelook_ecommerce"

BIGQUERY_TABLES = [
    "users",
    "orders",
    "order_items",
    "products",
    "inventory_items",
    "distribution_centers",
]

# Snowflake Configuration
SNOWFLAKE_ACCOUNT = "NWCZSXF-HM78006"
SNOWFLAKE_DATABASE = "DB_ERP"
SNOWFLAKE_WAREHOUSE = "DEV_WH"
SNOWFLAKE_ROLE = "role_dev"
SNOWFLAKE_USER = "FCM"
SNOWFLAKE_BRONZE_SCHEMA = "BRONZE"
SNOWFLAKE_SILVER_SCHEMA = "SILVER"
SNOWFLAKE_GOLD_SCHEMA = "GOLD"
