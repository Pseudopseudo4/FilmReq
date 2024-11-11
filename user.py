import os
import sys
from search_algo import *

class User():
    def __init__(self, username):

        self.load_user(username)
    
    def load_user(self, username):

        #Obtient la position du fichier
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.abspath(".")

        save_folder = os.path.join(base_dir, "userinfo")

        file_path = os.path.join(save_folder, username+"_userinfo.txt")

        with open(file_path, 'r') as file:

            #Met les lignes de l'information d'utilisateur dans une liste
            lines = file.readlines()

            self.prenom = lines[0]
            self.nom = lines[1]
            self.langue = lines[2]

            self.films_aime = [int(num) for num in lines[3].split(',')[:-1]]
            
            self.film_aime_pas = [int(num) for num in lines[4].split(',')[:-1]]

            self.rate_tags()

    def rate_tags(self):

        tags = {}

        #Aimé
        for film in self.films_aime:

            movie_tags = get_movie_tags(film)

            for tag in movie_tags:
                if tags.get(tag) is None:
                    tags[tag] = 0
                tags[tag]+=1

        #Pas Aimé
        for film in self.film_aime_pas:

            movie_tags = get_movie_tags(film)

            for tag in movie_tags:
                if tags.get(tag) is None:
                    tags[tag] = 0
                tags[tag]-=1

        final_tags = {}

        for tag in tags:
            if tags[tag] != 0:
                final_tags[tag] = tags[tag]

        self.tags = final_tags