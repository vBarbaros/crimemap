import pymysql
from dbconfig import DB_CONFIG
   

class DBHelper:
    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
            user=DB_CONFIG['db_user'],
            passwd=DB_CONFIG['db_password'],
            db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()
     
    def add_input(self, data):
        connection = self.connect()
        try:
            # The following introduces a deliberate security flaw.
            #See section on SQL injection below
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
     
    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()