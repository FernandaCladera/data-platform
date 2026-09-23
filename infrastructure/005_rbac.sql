-- Administrative setup

use role accountadmin;

-- role
create role if not exists role_dev;

-- compute access
grant usage  on warehouse dev_wh to role role_dev;

-- database access
grant usage on database db_erp to role role_dev;

-- schema access
grant usage on schema db_erp.bronze to role role_dev;
grant usage on schema db_erp.silver to role role_dev;
grant usage on schema db_erp.gold to role role_dev;

-- object/action permissions
grant create table on schema db_erp.bronze to role role_dev;
grant create table on schema db_erp.silver to role role_dev;
grant create table on schema db_erp.gold to role role_dev;
grant create view on schema db_erp.bronze to role role_dev;
grant create view on schema db_erp.silver to role role_dev;
grant create view on schema db_erp.gold to role role_dev;
grant create schema on database db_erp to role role_dev;

-- assign role to user
grant role role_dev to user FCM;

-- check
show grants to role role_dev;

-- start working
use role role_dev;