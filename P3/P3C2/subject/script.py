import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.woodbrass.com/guitares/guitares+electriques"
reponse = requests.get(url)
page = reponse.content

soup = BeautifulSoup(page, "html.parser")

titres = soup.find_all("h2")
titre_textes = []
f = open("outfile.txt", "w")
for titre in titres:
	titre_textes.append(titre.string)
	f.write(titre.string + "\n")

descriptions = soup.find_all("li")
description_textes = []
for description in descriptions:
	description_textes.append(description.string)
	if description.string:
		f.write(description.string + "\n")
f.close()