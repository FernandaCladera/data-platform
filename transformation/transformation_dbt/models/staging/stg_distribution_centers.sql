{{config (materialized='view', schema='silver')}}
select
    id as distribution_center_id,
    name as distribution_center_name,
    latitude,
    longitude,
    distribution_center_geom
from {{source('bronze','distribution_centers')}}
