import pyodbc
from config import SERVER, DATABASE, USER, PASSWORD

def connect():
    try:
        global cnxn
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER+';PWD='+ PASSWORD)
        global cursor
        cursor = cnxn.cursor()
        print("Conectado ao Banco de dados. ")
    except:
        print("Houve um erro ao conectar ao Banco de dados. ")
