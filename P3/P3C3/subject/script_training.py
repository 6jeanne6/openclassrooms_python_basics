import requests
from bs4 import BeautifulSoup
import csv

###the aim of this exercise is to reorder instructions into functions

def scrap_that_website():
	url = "https://www.gov.uk/search/news-and-communications"
	response = requests.get(url)
	page = response.content
	soup = BeautifulSoup(page, "html.parser")
	elements = soup.find_all("li", class_="gem-c-document-list__item")
	return elements

def transform(elements):
	results = []
	for element in elements:
		titre = element.find("a", class_="govuk-link")
		description = element.find("p", class_="gem-c-document-list__item-description")
		donnee = (titre.string, description.string)
		results.append(donnee)
	return results
     
def create_csv(data):
	header = ["title", "description"]
	with open("data.csv", "w", newline="") as fichier_csv:
		#create writer object to write in CSV file
		writer = csv.writer(fichier_csv, delimiter=",")
		#write first row
		writer.writerow(header)
		for donnee in data:
			writer.writerow(donnee)

def main():
	elements = scrap_that_website()
	data = transform(elements)
	create_csv(data)
	print("📁 Your data.csv has been created 📁")

if __name__ == "__main__":
    main()