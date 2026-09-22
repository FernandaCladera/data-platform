{{ config(materialized='view', schema='SILVER') }}

select
    id as product_id,
    cost,
    category,
    name as product_name,
    brand,
    retail_price,
    department,
    sku,
    distribution_center_id
from {{ source('bronze', 'products') }}