import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailsender():
    hostname = ""
    port = 587
    username = ""
    password = ""
    recipient = ""
    connection = None

    def __init__(self, hostname, port, username, password, recipient):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.recipient = recipient

    def connect(self):
        self.connection = smtplib.SMTP(host=self.hostname, port=self.port)
        self.connection.starttls()
        self.connection.login(self.username, self.password) 
        print(self.connection)
    
    def sendMessage(self, name, priceWish, vendor, url):
        subject = "{} is cheaper then {}".format(name, priceWish)

        text = "{} is cheaper then {} at {}.\n \tLink: {}".format(name, priceWish, vendor, url)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        self.connection.sendmail(self.username,self.recipient,message)
        