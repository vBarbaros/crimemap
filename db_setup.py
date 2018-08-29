import pymysql
from crimeapp import DB_CONFIG
   
connection = pymysql.connect(host='localhost',
                     user=DB_CONFIG.get_user(),
                     passwd=DB_CONFIG.get_pwd())
try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
            id int NOT NULL AUTO_INCREMENT,
            latitude FLOAT(10,6),
            longitude FLOAT(10,6),
            date DATETIME,
            category VARCHAR(50),
            description VARCHAR(1000),
            updated_at TIMESTAMP,
            PRIMARY KEY (id)
            )"""
        cursor.execute(sql);
        connection.commit()
finally:
    connection.close()