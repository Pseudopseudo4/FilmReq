import pandas as pd
import csv
from csv import DictReader

##df = pd.read_csv('https://www.donneesquebec.ca/recherche/dataset/1d291579-a5ec-41e6-af4b-c8dfa293c025/resource/c6393097-24f7-4de3-8909-086733afd7c0/download/extract_video_20241027.csv', encoding="Windows-1252", on_bad_lines='skip')

# Write the results to a different file
file = 'banque_de_films.csv'
 
def search(criteria):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if match(criteria, row['TITRE_245a']):
                print(row['TITRE_245a'], row['NB_ITEMS'])

def match(criteria, title):
    if criteria.lower() in title.lower():
        return True
    else:
        return False


search('star')

#print(data['TITRE_245a'])