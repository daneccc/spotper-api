import pyodbc
from config import SERVER, DATABASE, USER, PASSWORD

def connect():
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER+';PWD='+ PASSWORD)
        cursor = cnxn.cursor()
        print("Conectado ao Banco de dados. ")
        return cnxn, cursor
    except:
        print("Houve um erro ao conectar ao Banco de dados. ")

cnxn, cursor = connect()