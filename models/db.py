import mysql.connector
from mysql.connector import Error

#Conexão com o BD mySQL
def conectBD():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="lorraine1",
            database="clincontrol"
        )
    except Error as e:
        print("Error ao conctar ao Banco", e)

   