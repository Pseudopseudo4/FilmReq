import pandas as pd
import csv
from csv import DictReader

file = 'extract.csv'

def cleanMovies():

    #Call the movies file, using only the necessary columns
    df = pd.read_csv(file, encoding="Windows-1252", on_bad_lines='skip', usecols=['TITRE_245a', 'DUREE_CONTENU', 'PRODUCTION_264B', 'LANGUE_PRINCIPALE_1017', 'CATEGORIE', 'SOUS_CATEGORIE', 'DATE_PRODUCTION_046K'])

    #Remove movies with duplicate names (happens because of sequels and movies that don't have their subtitle entered)
    df = df.drop_duplicates()

    #Remove collections from the movies and shows

    return df