import mysql.connector 
from mysql.connector import Error

#TODO: run pip install mysql-connector-python bcrypt customtkinter

def get_dbConnection():
    try:
        connection = mysql.connector.connect ( #pafill up nalang po thank u
            host = 
            user = 
            password = 
            db = 
        )
        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Cannot cnnect to mySql {e}")