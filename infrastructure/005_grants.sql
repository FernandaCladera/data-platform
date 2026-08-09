use role accountadmin;
show grants on warehouse dev_wh;
grant usage on warehouse dev_wh to role role_dev;
grant role role_dev to user fernandac;
grant all on database db_erp to role role_dev;

use role role_dev;
