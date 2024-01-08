import logging 
import datetime 
import os 
out_path='C:/Users/ravik/PycharmProjects/projects/db_to_csv/logs'
file_name="db_to_csv"
log_filename = out_path+'/'+datetime.datetime.now().strftime("%Y-%m-%d") + file_name+'.log'
logging.basicConfig(
filename=log_filename,
level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(message)s',
filemode='w',
)   





