DROP TABLE IF EXISTS DB_ERP.BRONZE.DISTRIBUTION_CENTERS;

CREATE TABLE DB_ERP.BRONZE.DISTRIBUTION_CENTERS (
    id NUMBER,
    name VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    distribution_center_geom GEOGRAPHY
);


DROP TABLE IF EXISTS DB_ERP.BRONZE.INVENTORY_ITEMS;

CREATE TABLE DB_ERP.BRONZE.INVENTORY_ITEMS (
    id NUMBER,
    product_id NUMBER,
    created_at TIMESTAMP_TZ,
    sold_at TIMESTAMP_TZ,
    cost FLOAT,
    product_category VARCHAR,
    product_name VARCHAR,
    product_brand VARCHAR,
    product_retail_price FLOAT,
    product_department VARCHAR,
    product_sku VARCHAR,
    product_distribution_center_id NUMBER
);


DROP TABLE IF EXISTS DB_ERP.BRONZE.ORDERS_ITEMS;

CREATE TABLE DB_ERP.BRONZE.ORDERS_ITEMS (
    id NUMBER,
    order_id NUMBER,
    user_id NUMBER,
    product_id NUMBER,
    inventory_item_id NUMBER,
    status VARCHAR,
    created_at TIMESTAMP_TZ,
    shipped_at TIMESTAMP_TZ,
    delivered_at TIMESTAMP_TZ,
    returned_at TIMESTAMP_TZ,
    sale_price FLOAT
);


DROP TABLE IF EXISTS DB_ERP.BRONZE.PRODUCTS;

CREATE TABLE DB_ERP.BRONZE.PRODUCTS (
    id NUMBER,
    cost FLOAT,
    category VARCHAR,
    name VARCHAR,
    brand VARCHAR,
    retail_price FLOAT,
    department VARCHAR,
    sku VARCHAR,
    distribution_center_id NUMBER
);


DROP TABLE IF EXISTS DB_ERP.BRONZE.USERS;

CREATE TABLE DB_ERP.BRONZE.USERS (
    id NUMBER,
    first_name VARCHAR,
    last_name VARCHAR,
    email VARCHAR,
    age NUMBER,
    gender VARCHAR,
    state VARCHAR,
    street_address VARCHAR,
    postal_code VARCHAR,
    city VARCHAR,
    country VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    traffic_source VARCHAR,
    created_at TIMESTAMP_TZ,
    user_geom GEOGRAPHY
);