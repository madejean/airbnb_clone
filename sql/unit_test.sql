/*created database and user for testing*/

CREATE USER 'airbnb_user_test'@'%' IDENTIFIED BY 'password';

CREATE DATABASE airbnb_test CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON airbnb_test.* TO 'airbnb_user_test'@'%';
