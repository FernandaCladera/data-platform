--TRUNCATE TABLE DB_ERP.BRONZE.DISTRIBUTION_CENTERS;
--TRUNCATE TABLE DB_ERP.BRONZE.INVENTORY_ITEMS;
--TRUNCATE TABLE DB_ERP.BRONZE.ORDER_ITEMS;
--TRUNCATE TABLE DB_ERP.BRONZE.PRODUCTS;
--TRUNCATE TABLE DB_ERP.BRONZE.USERS;

--select * from db_erp.bronze.ORDER_ITEMS limit 3;

--select distinct status from db_erp.bronze.ORDER_ITEMS

--SELECT *
--FROM DB_ERP.BRONZE_GOLD.DIM_PRODUCTS
--WHERE product_name IS NULL;

drop schema if exists db_erp.bronze_bronze cascade;
--drop schema if exists db_erp.bronze_gold cascade;