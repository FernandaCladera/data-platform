
{{ config (materialized='table', schema='GOLD') }}

select
    product_id,
    coalesce(product_name, 'Unknown') as product_name,
    brand,
    category,
    department,
    sku,
    cost,
    retail_price,
    distribution_center_id
from {{ref('stg_products')}}
