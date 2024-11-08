import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cleanMovies import *

df = cleanMovies()

class Accueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Button for "Nouvel utilisateur"
        self.button_nouv = ctk.CTkButton(self, text="Nouvel utilisateur", command=self.button_nouv)
        self.button_nouv.grid(row=0, column=0, pady=(20,10))
        
        # Ensure df['CATEGORIE'] exists before proceeding
        if 'CATEGORIE' in df.columns:
            # Calculate category distribution and filter out low-percentage categories
            category_counts = df['CATEGORIE'].value_counts(normalize=True) * 100
            threshold = 2  # Define the minimum percentage threshold for display
            major_categories = category_counts[category_counts >= threshold]
            minor_categories = category_counts[category_counts < threshold].sum()

            # Add 'Other' category if there are minor categories
            if minor_categories > 0:
                major_categories['Other'] = minor_categories
            
            # Create the pie chart
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(major_categories, labels=major_categories.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Percentage Distribution of Categories")

            # Embed the pie chart in Tkinter
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=0, pady=(10, 0))


    def button_nouv(self):
        self.master.show_creaProfil()