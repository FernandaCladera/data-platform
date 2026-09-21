DROP TABLE IF EXISTS DB_ERP.BRONZE.ORDERS;
CREATE TABLE DB_ERP.BRONZE.ORDERS (
    order_id NUMBER,
    user_id NUMBER,
    status VARCHAR,
    gender VARCHAR,
    created_at TIMESTAMP_TZ,
    returned_at TIMESTAMP_TZ,
    shipped_at TIMESTAMP_TZ,
    delivered_at TIMESTAMP_TZ,
    num_of_item NUMBER
);