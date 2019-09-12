import loadconfig
import PriceChecker
import sendMails

import time
import datetime


banner = """
         .______   .______       __    ______  _______               
         |   _  \  |   _  \     |  |  /      ||   ____|              
         |  |_)  | |  |_)  |    |  | |  ,----'|  |__                 
         |   ___/  |      /     |  | |  |     |   __|                
         |  |      |  |\  \----.|  | |  `----.|  |____               
         | _|      | _| `._____||__|  \______||_______|              
                                                                     
  ______  __    __   _______   ______  __  ___  _______ .______      
 /      ||  |  |  | |   ____| /      ||  |/  / |   ____||   _  \     
|  ,----'|  |__|  | |  |__   |  ,----'|  '  /  |  |__   |  |_)  |    
|  |     |   __   | |   __|  |  |     |    <   |   __|  |      /     
|  `----.|  |  |  | |  |____ |  `----.|  .  \  |  |____ |  |\  \----.
 \______||__|  |__| |_______| \______||__|\__\ |_______|| _| `._____|
                                                                     """

print(banner)

config = loadconfig.ConfigReader("./config.json")

mailConfig = config.getMailConfig()
Maildemon = sendMails.Mailsender(mailConfig["smtpServer"],mailConfig["smtpPort"],mailConfig["username"],mailConfig["password"],mailConfig["recipient"])
Maildemon.connect()
items = config.getItems()

print("Generate Price Checker")
checker = []
for item in items:
    checker.append(PriceChecker.priceChecker(item["url"],item["priceWish"],item["vendor"],item["name"]))

while True:
    if (datetime.datetime.now().time().hour == 19 or datetime.datetime.now().time().hour == 20) and datetime.datetime.now().time().minute == 14:
        for check in checker:
            if check.comparePrice(check.getPrice()):
                Maildemon.sendMessage( check.name, check.priceWish, check.vendor, check.product_uri)
        time.sleep(60)
    else:
        time.sleep(60)
