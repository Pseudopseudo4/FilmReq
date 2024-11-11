import pandas as pd
import string
import math
import os
import sys

def translate_date(x):

    date = ''.join(filter(str.isdigit, str(x)))

    if date != '':
        x = int(float(date[0:4]))

        if x < 1950:
            return "-1950"
        elif x > 2020:
            return "+2020"
        else:
            min = math.floor(x/10)*10
            max = min+10
            return str(min)+"-"+str(max)
    return ''

def translate_duree(x):

    duree = 0

    x = x.replace(" ","")

    #Calcule la duree de film en minute
    if "h" in x:
        end_pos = x.find("h")
        n_string = ''.join(filter(str.isdigit, str(x[0:end_pos])))
        duree+= int(n_string)*60
        x = x[end_pos+1:len(x)]

    if "min" in x:
        end_pos = x.find("min")
        n_string = ''.join(filter(str.isdigit, str(x[0:end_pos])))
        duree+= int(n_string)

    if duree > 240:
        duree = 0

    #Transforme la duree en plage de temps
    if duree >= 240:
        return ""
    elif duree >= 180:
        return "+180 min"
    elif duree >= 120:
        return "120-180 min"
    elif duree >= 90:
        return "90-120 min"
    elif duree >= 40:
        return "45-90 min"
    else:
        return ""

    return duree

def clean_file(file):

    with open(file, newline='') as f:

        new_file = []

        #Verifie chaque ligne pour supprimer les charactere " de trop
        for line in f:
            
            fake_quote = False
            start_string = False
            new_line = ""
            normalized_line = line.replace("\n","") #Enleve les breaklines

            for i in range(len(normalized_line)):
                
                character = normalized_line[i]

                if character == '"':
                    if start_string and not fake_quote and ((i < len(normalized_line)-1 and normalized_line[i+1] == ',') or i == len(normalized_line)-1):
                        start_string = False
                        new_line+=character
                    elif not start_string and not fake_quote and ((i > 0 and normalized_line[i-1] == ',') or i == 0):
                        start_string = True
                        new_line+=character
                    else:
                        new_line+=""
                        fake_quote = not fake_quote
                            
                else:
                    new_line+=character
            
            new_file.append(new_line+"\n")

    #Ouvre le fichier csv pour ecrire les nouvelles lignes
    with open(file, 'w') as f: 
        f.writelines(new_file)

def clean_dataframe(file):

    #Trouve l'emplacement du fichier csv
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    # Define the path to the bundled movie.csv file
    file_path = os.path.join(base_path, file)

    #Utilise seulement les colonnes necessaires
    df = pd.read_csv(file_path, encoding="Windows-1252", on_bad_lines='skip', usecols=['TITRE_245a', 'DUREE_CONTENU', 'PRODUCTION_264B', 'LANGUE_PRINCIPALE_1017', 'CATEGORIE', 'SOUS_CATEGORIE', 'DATE_PRODUCTION_046K'])

    #Supprime les titre ambigus ou trop similaires
    df['TITRE_245a'] = df['TITRE_245a'].map(lambda x: string.capwords(x.replace('--', '').replace(' :', '').strip().lower()) if isinstance(x, str) else x)
    df = df.drop_duplicates(subset=['TITRE_245a'])
    df = df.dropna()

    #Supprime les titres d'une duree de plus de 240 minutes

    #Ajoute les categories d'annee
    df['DATE_PRODUCTION_046K'] = df['DATE_PRODUCTION_046K'].map(translate_date)

    #Ajoute les categories de duree
    df['DUREE_CONTENU'] = df['DUREE_CONTENU'].map(translate_duree)

    return df

df = clean_dataframe('movie_list.csv')

def get_all_tags(tag):

    tag = tag.lower()

    return_list = []

    if tag == "date":

        #Retourne une liste de tuple pour determiner la plage de date de film
        return_list = ["-1950", "1950-1960", "1960-1970", "1970-1980", "1980-1990", "1990-2000", "2000-2010", "2010-2020", "+2020"]

    elif tag == "duree":

        #Retourn une liste de tuple pour determiner la plage de duree de film (m)
        return_list = ["45-90 min", "90-120 min", "120-180 min", "+180 min"]

    elif tag == "langue":

        #Retourn une liste de tuple pour determiner la plage de duree de film (m)
        return_list = df["LANGUE_PRINCIPALE_1017"][df["LANGUE_PRINCIPALE_1017"].str.contains("autre") == False][df["LANGUE_PRINCIPALE_1017"].str.contains("aucun") == False].unique().tolist()

    elif tag == "categorie":

        #Retourn une liste des categories
        return_list = df["CATEGORIE"][df["CATEGORIE"] != "N.A"][df["CATEGORIE"] != "SERIE TELEVISEE"].unique().tolist()

    elif tag == "sous-categorie":

        #Retourn une liste des sous-categories
        return_list = df["SOUS_CATEGORIE"][df["SOUS_CATEGORIE"] != "N.A"].unique().tolist()

    return return_list

def get_movie_tags(index): 

    columns = ['LANGUE_PRINCIPALE_1017', 'CATEGORIE', 'SOUS_CATEGORIE', 'DUREE_CONTENU', 'DATE_PRODUCTION_046K']
    tags = []

    if index < len(df)-1:

        for column in columns:
            
            string = df.iloc[index][column]

            if type(string) == str:
                words = string.split(', ')
            else:
                words = ""

            for tag in words:
                tags.append(tag)

    return tags


def get_movie_rating(pos,tags_compare):

    tags = get_movie_tags(pos)
    rating = 0

    for tag in tags:
        if tag in tags_compare:
            rating+=tags_compare[tag]

    return rating