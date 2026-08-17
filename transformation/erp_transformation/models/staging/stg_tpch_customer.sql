select
    c_acctbal as Account_Balance,
    c_address as Customer_Address,
    c_custkey as Customer_Key,
    c_mktsegment as Customer_Market_Segment,
    c_name as Customer_Name,
    c_nationkey as Nation_Key

from {{source('tpch','customer')}}