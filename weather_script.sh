#!/bin/bash

user='root'
password=''
database='weather_database'

sudo apt-get install python3-pip
pip install mysqlclient


echo -e "mysql install"
sudo apt install mysql-server -y

sudo mysql --user=$user --execute="CREATE DATABASE $database; USE $database; CREATE TABLE weather_table (temp INT(3), humidity INT(3), pressure INT(3)); "

sudo mysql --user=$user --execute="CREATE USER 'weather_user'@'localhost' IDENTIFIED BY ''; GRANT ALL ON *.* TO 'weather_user'@'localhost'; FLUSH PRIVILEGES;"
