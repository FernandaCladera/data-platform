{{ config (materialized='table', schema='GOLD')}}
with order_items as (
    select *
    from {{ref('stg_orders_items')}}
),

products as (
    select *
    from {{ref('stg_products')}}
),

final as (
    select
        {{dbt_utils.generate_surrogate_key([
            'oi.order_id',
            'oi.order_item_id',
        ])}} as sales_key,

        oi.order_item_id,
        oi.order_id,
        oi.user_id,
        oi.product_id,
        oi.inventory_item_id,
        oi.status as order_status,
        oi.created_at as ordered_at,
        oi.shipped_at,
        oi.delivered_at,
        oi.returned_at,
        oi.sale_price,
        p.cost,
        {{calculate_gross_profit ('oi.sale_price', 'p.cost')}} as gross_profit,
        {{calculate_gross_margin ('oi.sale_price', 'p.cost')}} as gross_margin

    from order_items oi
    left join products p on oi.product_id = p.product_id
)

select * from final
