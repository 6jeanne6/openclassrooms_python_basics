import requests
from bs4 import BeautifulSoup
import csv

#extract data in the input file inside a list
def extract():
    data = []
    with open("input.csv", "r") as source_csv:
           freading = csv.DictReader(source_csv, delimiter=',')
           for row in freading:
                 data.append(row)
    return data

#transform the data    
def transform(data):
      for wage in data:
            hour = wage["heures_travaillees"]
            wage["heures_travaillees"] = int(hour) * 15

#load into the output file
def load(data):
	header = ['name', 'wage']
	with open("output.csv", "w") as result_csv:
            writer = csv.writer(result_csv, delimiter=',')
            writer.writerow(header)
            for row in data:
                   newdata = (row["nom"], row["heures_travaillees"])
                   writer.writerow(newdata) 

def main():
    data = extract()
    transform(data)
    load(data)
    print("📁 Your output.csv has been created 📁")

if __name__ == "__main__":
    main()
