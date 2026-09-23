
{{config (materialized='table',schema='gold')}}
select
    inventory_item_id,
    product_id,
    created_at,
    sold_at,
    cost,
    product_category,
    product_name,
    product_brand,
    product_retail_price,
    product_department,
    product_sku,
    distribution_center_id,
    case when sold_at is not null then 'sold' else 'available' end as inventory_status
from {{ ref('stg_inventory_items') }}