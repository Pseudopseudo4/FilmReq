import pandas as pd
import csv
import string
from csv import DictReader

file = 'extract.csv'

def cleanMovies():

    #Call the movies file, using only the necessary columns
    df = pd.read_csv(file, encoding="Windows-1252", on_bad_lines='skip', usecols=['TITRE_245a', 'DUREE_CONTENU', 'PRODUCTION_264B', 'LANGUE_PRINCIPALE_1017', 'CATEGORIE', 'SOUS_CATEGORIE', 'DATE_PRODUCTION_046K'])

    #Removes ambiguous titles, with empty : or other characters
    df['TITRE_245a'] = df['TITRE_245a'].map(lambda x: string.capwords(x.replace('--', '').replace(' :', '').strip().lower()) if isinstance(x, str) else x)
    df = df.drop_duplicates(subset=['TITRE_245a'])

    #Remove collections from the movies and shows (multiple time numbers)

    return df

df = cleanMovies()

def get_movie_name(pos):
    return df.iloc[pos]["TITRE_245a"]

def get_movie_tags(index): 

    columns = ['LANGUE_PRINCIPALE_1017', 'CATEGORIE', 'SOUS_CATEGORIE']
    tags = []

    for column in columns:
        for tag in df.iloc[index][column].split(', '):
            tags.append(tag)

    return tags

cleanMovies()