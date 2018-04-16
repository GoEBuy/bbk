DROP DATABASE IF EXISTS bbk;
CREATE DATABASE IF NOT EXISTS bbk DEFAULT CHARSET utf8 COLLATE utf8_general_ci; 

CREATE USER 'username'@'host' IDENTIFIED BY 'password';


GRANT privileges ON databasename.tablename TO 'username'@'host';
FLUSH privileges;


