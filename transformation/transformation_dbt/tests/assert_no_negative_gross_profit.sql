select *
from {{ ref ('fct_sales') }}
where gross_profit < 0