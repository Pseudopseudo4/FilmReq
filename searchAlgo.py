import pandas as pd
import csv
from csv import DictReader
from cleanMovies import *

file = 'extract.csv'
df = cleanMovies()

def searchByTitle(title_name):
    """
    Search movie or show by name
    """

    with open(file, newline='') as csvfile:

        #Set dataframe as dictionary
        reader = df.to_dict(orient='records')

        #Return array
        r = []

        #Check every row
        for row in reader:    
            #If the entered search is present in title, return it
            if matchTitle(title_name, row['TITRE_245a']):
                r.append(row['TITRE_245a'])
        
        return r

def matchTitle(searched_title, compared_title):
    """
    Defines the necessary criteria to be met when checking if search corresponds to value
    """
    
    #Create list of every word in search
    words = searched_title.split(" ")

    #Check to see if every word is in the title
    for i in range(len(words)):
        if words[i].lower() not in compared_title.lower():
            return False
    return True

def searchTag(tag_name):
    """
    Search tag by name
    """