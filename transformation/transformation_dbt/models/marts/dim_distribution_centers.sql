{{ config (materialized='table',schema='GOLD')}}

select
    distribution_center_id,
    distribution_center_name,
    latitude,
    longitude,
    distribution_center_geom
from {{ref('stg_distribution_centers')}}
