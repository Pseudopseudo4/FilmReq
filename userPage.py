import customtkinter as ctk
import tkinter as tk
import pandas as pd
import os
from pandastable import Table
from searchAlgo import *
from user import *

class UserPage(ctk.CTkFrame):

    def __init__(self, parent):

        #Frame pour la page complete
        self.main_frame = ctk.CTkFrame(parent)
        self.main_frame.pack()
        
        #Frame pour l'information personelle
        self.info_frame = ctk.CTkFrame(self.main_frame)
        self.info_frame.pack(fill="x")

        # Nom
        self.name_label = ctk.CTkLabel(self.info_frame, text="Nom:")
        self.name_label.pack(side="left",padx=5,pady=5)
        self.name_entry = ctk.CTkEntry(self.info_frame, placeholder_text="Entrez votre nom")
        self.name_entry.pack(side="left",padx=5,pady=5)

        # Prénom
        self.firstname_label = ctk.CTkLabel(self.info_frame, text="Prénom:")
        self.firstname_label.pack(side="left",padx=5,pady=5)
        self.firstname_entry = ctk.CTkEntry(self.info_frame, placeholder_text="Entrez votre prénom")
        self.firstname_entry.pack(side="left",padx=5,pady=5)

        # Langue
        languages = df['LANGUE_PRINCIPALE_1017'].dropna().unique().tolist()
        self.langue_label = ctk.CTkLabel(self.info_frame, text="Langue:")
        self.langue_label.pack(side="left",padx=5,pady=5)
        
        self.langue_option = ctk.CTkOptionMenu(self.info_frame, values=languages)
        self.langue_option.pack(side="left",padx=5,pady=5)
        self.langue_option.set("Sélectionnez la langue")

        #Frame pour les films
        self.films_frame = ctk.CTkFrame(self.main_frame)
        self.films_frame.pack(fill="x")     

        #Film aimé/non
        self.liked_movies       = UserMoviesList(self.films_frame, "Films Aimés", 300, "left")
        self.disliked_movies    = UserMoviesList(self.films_frame, "Films Pas Aimés", 300, "right")

        #Frame pour la sauvegarde ou efface de profil
        self.controle_frame = ctk.CTkFrame(self.main_frame)
        self.controle_frame.pack(fill="x")

        #Bouton sauvegarde
        self.save_button = ctk.CTkButton(self.controle_frame, text="Sauvegarder", width=30, command=lambda : self.save_user())
        self.save_button.pack(padx=5,pady=5,side="left")

        """
        self.delete_button = ctk.CTkButton(self.controle_frame, text="Supprimer", width=30, fg_color="red", hover_color="darkred", command=lambda : self.delete_user())
        self.delete_button.pack(padx=5,pady=5,side="right")
        """

    def save_user(self):

        file_path = os.path.join("userinfo", self.name_entry.get()+self.firstname_entry.get()+"_userinfo.txt")

        #Sauvegarder vers un fichier l'info d'utilisateur
        with open(file_path, "w") as file:
            
            file.write(self.name_entry.get()+"\n")
            file.write(self.firstname_entry.get()+"\n")
            file.write(self.langue_option.get()+"\n")

            for name, id in self.liked_movies.movies:
                file.write(str(id)+",")
            file.write("\n")

            for name, id in self.disliked_movies.movies:
                file.write(str(id)+",")
            file.write("\n")

            

            file.write("\n")