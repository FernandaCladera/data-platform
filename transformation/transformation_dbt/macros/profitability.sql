
{% macro calculate_gross_profit(sale_price, cost) %}
    ({{ sale_price }} - {{ cost }})
{% endmacro %}

{% macro calculate_gross_margin(sale_price, cost) %}
    ({{ sale_price }} - {{ cost }}) / {{ sale_price }}
{% endmacro %}