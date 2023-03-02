#!/bin/bash

user='root'
password=''
database='weather_database'

sudo apt-get install python3-pip
pip install mysql-connector-python


echo -e "mariadb install"
sudo apt-get install mariadb-server

sudo mysql --user=$user --execute="CREATE DATABASE $database; USE $database; CREATE TABLE weather_table (date DATE, temp INT(3), humidity INT(3), pressure INT(3)); "

sudo mysql --user=$user --execute="CREATE USER 'weather_user'@'localhost' IDENTIFIED BY ''; GRANT ALL ON *.* TO 'weather_user'@'localhost'; FLUSH PRIVILEGES;"

eval "$(curl -o pi_weather.py  https://raw.githubusercontent.com/TerryDennisonJr/weather_pi/main/weather_app_mysql.py)"
