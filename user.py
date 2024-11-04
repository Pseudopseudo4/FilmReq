import customtkinter as ctk
import tkinter as tk
import pandas as pd
from pandastable import Table

# Load data
df = pd.read_csv("extract.csv", encoding="Windows-1252", on_bad_lines='skip', 
                 usecols=['TITRE_245a', 'DUREE_CONTENU', 'PRODUCTION_264B', 
                          'LANGUE_PRINCIPALE_1017', 'CATEGORIE', 
                          'SOUS_CATEGORIE', 'DATE_PRODUCTION_046K'])

#ctk.set_appearance_mode("dark")
#ctk.set_default_color_theme("blue") 

class User(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        # Grille
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Nom
        self.name_label = ctk.CTkLabel(self, text="Nom:")
        self.name_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Entrez votre nom")
        self.name_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        # Prénom
        self.firstname_label = ctk.CTkLabel(self, text="Prénom:")
        self.firstname_label.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
        self.firstname_entry = ctk.CTkEntry(self, placeholder_text="Entrez votre prénom")
        self.firstname_entry.grid(row=1, column=1, padx=20, pady=(20, 10), sticky="ew")

        # Langue
        languages = df['LANGUE_PRINCIPALE_1017'].dropna().unique().tolist()
        self.langue_label = ctk.CTkLabel(self, text="Langue:")
        self.langue_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
        
        self.langue_option = ctk.CTkOptionMenu(self, values=languages)
        self.langue_option.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="ew")
        self.langue_option.set("Sélectionnez la langue")


#root = ctk.CTk()
#root.geometry("400x300")

#app = User(master=root)
#app.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

#root.mainloop()