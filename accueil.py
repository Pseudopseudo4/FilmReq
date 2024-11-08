import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cleanMovies import *
import os

df = cleanMovies()



class Accueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        
        list = os.listdir("userinfo")

        for user in list:

            with open(user, 'r') as file:
                nom = file.readlines()[0]
                
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        
        self.button_nouv = ctk.CTkButton(self, text=nom or "Nouvel utilisateur", command=self.button_nouv)


        self.button_nouv.grid(row=0, column=0, pady=(20,10))
        
        
        if 'CATEGORIE' in df.columns:
            
            category_counts = df['CATEGORIE'].value_counts(normalize=True) * 100
            threshold = 2  
            major_categories = category_counts[category_counts >= threshold]
            minor_categories = category_counts[category_counts < threshold].sum()

            
            if minor_categories > 0:
                major_categories['Other'] = minor_categories
            
           
            fig, ax = plt.subplots(figsize=(4, 4))
            ax.pie(major_categories, labels=major_categories.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Distribution des catégories")

            
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=0, pady=(0, 0))

        if 'SOUS_CATEGORIE' in df.columns:
            
            category_counts = df['SOUS_CATEGORIE'].value_counts(normalize=True) * 100
            threshold = 4  
            major_categories = category_counts[category_counts >= threshold]
            minor_categories = category_counts[category_counts < threshold].sum()

            
            if minor_categories > 0:
                major_categories['Other'] = minor_categories
            
           
            fig, ax = plt.subplots(figsize=(4, 4))
            ax.pie(major_categories, labels=major_categories.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Distribution des sous_catégories")

            
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=2, column=0, pady=(0, 0))


    def button_nouv(self):
        self.master.show_creaProfil()