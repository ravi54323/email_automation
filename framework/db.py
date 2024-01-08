import pyodbc 
from log import *
logging.info("Etrablishing sql connection")
try:
    def db_connection(SERVER,DATABASE,UID,PWD):
        connection_string = f"Driver={{SQL Server}};Server={SERVER};Database={DATABASE};Uid={UID};Pwd={PWD};"
        conn = pyodbc.connect(connection_string)
        cursor=conn.cursor() 
        return cursor 
except Exception:
    logging.info("Got error while connecting to sql and the error is ")







