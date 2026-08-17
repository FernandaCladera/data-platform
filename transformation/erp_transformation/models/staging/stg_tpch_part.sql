select
    p_brand as part_brand,
    p_type as part_type,
    p_size as part_size,
    p_container as part_container,
    p_retailprice as part_retail_price,
    p_name as part_name
from 
    {{ source ('tpch','part') }}