###Data extraction from web
from bs4 import BeautifulSoup

#it closes automatically
with open("index.html", "r") as file:
	soup = BeautifulSoup(file.read(), 'html.parser')

#store all what's inside <li></li>
products = soup.find_all('li')

#handling dictionaries
my_products = {}

#in p tag find class_="price"
for product in products:
	name = product.find('h2').string
	price_list = product.find('p', class_="price").string
	price = price_list.split(' ')
	my_products[name] = {"price": price[1]}

description_list = []
#-1 is the last element found with p tag
for product in products:
	name = product.find('h2').string
	description = product.find_all("p")[-1].string
	description = description.strip("Description :")
	my_products[name]["description"] = description

#use round() to set numbers of decimals with float
#convert € to $
for name in my_products.keys():
	price_string = my_products[name]["price"]
	price = price_string.strip('€')
	price = float(price)
	dollar_price = price * 1.2
	my_products[name]["price"] = f"{dollar_price}$"

print("All products in $: ", my_products)
