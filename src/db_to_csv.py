import sys
import configparser
import os 
sys.path.append('C:\\Users\\ravik\\PycharmProjects\\projects\\db_to_csv\\framework')
import db 
from log import * 
import mail

def sql_functios():
    try:
        cursor=db.db_connection(SERVER=config.get('DB','SERVER'),DATABASE=config.get('DB','DATABASE'),UID=config.get('DB','UID'),PWD=config.get('DB','PWD'))
        data=cursor.execute("select * from {}".format(config.get('DB','TABLE')))
        return data 
    except Exception as e:
        logging.error("Error message is : {}".format(str(e)))


if __name__== "__main__":

    config_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file)

    logging.info("program started here...")
    # Reading database and records
    data=sql_functios() 
    count=0
    if data:
        for i in data:
            #writing records into log files
            logging.info(i)
            count+=1 
    logging.info("Total no of records in the table {} is : {}".format(config.get('DB','TABLE'),count))

    #sending the log file to the email as attachment
    mail.email_preperation(config.get('MAIL','from_email'), config.get('MAIL','to_email'), config.get('MAIL','smtp_server'), config.get('MAIL','smtp_port'), config.get('MAIL','login_mail'), config.get('MAIL','password'))
