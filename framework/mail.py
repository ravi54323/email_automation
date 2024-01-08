import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from log import *

def email_preperation(from_email,to_email,smtp_server,smtp_port,login_mail,password):
    logging.info("started email preperation")
    try:
        subject = 'Mail testing today'
        message = 'Hello ravi i am testing today to send an email'

        # Create the email message
        to_email=to_email.split(',')
        for i in to_email:
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = i
            if i =='keshava.cadcam@gmail.com':
                msg['Subject'] = "Hi Dolu , i just tried to send an email using python script"
            else:
                msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            file_name='C:/Users/ravik/PycharmProjects/projects/db_to_csv/logs/'+datetime.datetime.now().strftime("%Y-%m-%d")+'db_to_csv.log'
            with open(file_name,'r') as f:
                attachment=MIMEApplication(f.read(),Name=basename(file_name))
                attachment['Content-Disposition'] = 'attachment;filename={}'.format(basename(file_name))
                msg.attach(attachment)
            # Create a secure connection to the SMTP server
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(login_mail, password)
                server.send_message(msg)
        logging.info("success fully sent an email in try block")
    except Exception as e:
        logging.ERROR("got some error and error is : {}".format(str(e)))

if __name__=='__main__':
    email_preperation(from_email, to_email, smtp_server, smtp_port, login_mail, password)
    logging.info("success fully sent an email in main block")