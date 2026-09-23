{{ config(materialized='table',schema='GOLD')}}

select
    user_id,
    first_name,
    last_name,
    email,
    age,
    gender,
    state,
    street_address,
    postal_code,
    city,
    country,
    latitude,
    longitude,
    traffic_source,
    created_at,
    user_geom
from {{ ref('stg_users') }}