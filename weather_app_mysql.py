from datetime import date, datetime
from datetime import date
import random
import time
import mysql.connector

cnx = mysql.connector.connect(
    user='weather_user', password='', database='weather_database')
cursor = cnx.cursor()

current = datetime.now().date()

while True:
    
    temp_val = int(sense.get_temperature())
    humi_val = int(sense.get_humidity())
    press_val = int(sense.get_pressure())

    print("Date", "\t\tTemperatue", "\tHumidity", "\Pressure")
    print(current, "\t", temp_val, "\t\t", humi_val, "\t\t", press_val)


    add_weather = ("INSERT INTO weather_table "
                   "(date, temp, humidity, pressure) "
                   "VALUES ( %(date)s, %(temp)s, %(humidity)s, %(pressure)s)")

    data_weather = {
        'date': current,
        'temp': temp_val,
        'humidity': humi_val,
        'pressure': press_val

    }
    cursor.execute(add_weather, data_weather)
    weather_id = cursor.lastrowid

    cnx.commit()

    cursor.close()
    cnx.close()

    time.sleep(5)
