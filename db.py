import mysql.connector
from mysql.connector import Error

#Conexão com o BD mySQL
def conectBD():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lorraine1",
            database="clincontrol"
        )
    except Error as e:
        print("Error ao conctar ao Banco", e)

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("Conexão encerrada")

conectBD()