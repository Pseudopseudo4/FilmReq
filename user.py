import customtkinter as ctk
import tkinter as tk
import pandas as pd
import os
from pandastable import Table
from searchAlgo import *

class User():
    def __init__(self, username):

        self.load_user(username)
    
    def load_user(self, username):
        
        file_path = os.path.join("userinfo", username+"_userinfo.txt")

        with open(file_path, 'r') as file:

            #Met les lignes de l'information d'utilisateur dans une liste
            lines = file.readlines()

            self.nom = lines[0]
            self.prenom = lines[1]
            self.langue = lines[2]

            self.films_aime = [int(num) for num in lines[3].split(',')[:-1]]
            
            self.film_aime_pas = [int(num) for num in lines[4].split(',')[:-1]]

            self.rate_tags()

    def rate_tags(self):

        self.tags = {}

        #Aimé
        for film in self.films_aime:

            movie_tags = get_movie_tags(film)

            for tag in movie_tags:
                if self.tags.get(tag) is None:
                    self.tags[tag] = 0
                self.tags[tag]+=1

        #Pas Aimé
        for film in self.film_aime_pas:

            movie_tags = get_movie_tags(film)

            for tag in movie_tags:
                if self.tags.get(tag) is None:
                    self.tags[tag] = 0
                self.tags[tag]-=1

    def delete_user(self):

        username = self.nom + self.prenom

        file_path = os.path.join("userinfo", username+"_userinfo.txt")

        #Supprime le fichier de sauvegarde
        if os.path.exists(username+"_userinfo.txt"):
            os.remove(username+"_userinfo.txt")

user = User("")