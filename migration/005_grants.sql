use role accountadmin;
show grants on warehouse dev_wh;
grant usage on warehouse dev_wh to role role_dev;


GRANT USAGE ON DATABASE DB_ERP TO ROLE ROLE_DEV;
GRANT USAGE ON SCHEMA DB_ERP.BRONZE TO ROLE ROLE_DEV;
GRANT CREATE VIEW ON SCHEMA DB_ERP.BRONZE TO ROLE ROLE_DEV;

SHOW GRANTS TO ROLE role_dev;

use role role_dev;