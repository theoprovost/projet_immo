-- Initial creation of the database and it's owner

DROP ROLE IF EXISTS "immo_admin";

-- CREATE USER|ROLE 'newuser'@'localhost' IDENTIFIED BY 'password';
CREATE ROLE "immo_admin" WITH PASSWORD 'e5679489-a4c8-445a-9036-0838a70de506';

DROP DATABASE IF EXISTS immo_db;

-- CREATE DATABASE 'database_name';
CREATE DATABASE immo_db;

-- Give privelegies to the role created just before
GRANT CONNECT ON DATABASE immo_db TO "immo_admin";
GRANT ALL PRIVILEGES ON DATABASE immo_db TO "immo_admin";
