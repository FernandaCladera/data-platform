use role accountadmin;
create warehouse if not exists dev_wh
warehouse_size= 'x-small'
auto_suspend= 60
auto_resume= true;
