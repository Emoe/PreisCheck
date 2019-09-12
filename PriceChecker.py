import re
import requests

class priceChecker():
	
	regex = {
		"saturn": r"<meta property=\"product:price:amount\" content=\"([\d\.]*)",
		"mediamarkt": r"<meta itemProp=\"price\" content=\"([\d\.]*)", 
		"cyberport": r"data-product-price=\"([\d\.]*)",
		"notebooksbilliger": r"data-price-formatted=\"([\d\.]*)"
	} 
	priceWish = 0
	product_uri = ""
	vendor = ""
	name = ""

	def __init__(self,product_uri,priceWish,vendor,name):
		self.priceWish = priceWish
		self.product_uri = product_uri
		self.vendor = vendor
		self.name = name

	def getPrice(self):
		priceReq = requests.get(self.product_uri)
		source = priceReq.text
	
		price = re.findall(self.regex[self.vendor], source)
		return price[0]
	
	def comparePrice(self,priceNow):
		if priceNow < self.priceWish:
			return True
		else:
			return False
	
