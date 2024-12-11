import customtkinter as ctk
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from movie_list_functions import clean_dataframe

file = "movie_list.csv"
df = clean_dataframe(file)



class Stats(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Frame pour les diagrammes
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5,pady=5)
        self.stat_frame.place(relx=0.5,rely=0.5,anchor="center")

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

            
            canvas = FigureCanvasTkAgg(fig, self.stat_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

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

            
            canvas = FigureCanvasTkAgg(fig, self.stat_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        self.durees_bouton = ctk.CTkButton(self, text="Durées", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_durees())
        self.durees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.durees_bouton.place(relx=0.40, rely=1, anchor='se')

        self.annees_bouton = ctk.CTkButton(self, text="Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees())
        self.annees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_bouton.place(relx=0.50, rely=1, anchor='se')

        self.langues_bouton = ctk.CTkButton(self, text="Langues", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_langues())
        self.langues_bouton.pack(side="left",padx=(0,5), pady=5)
        self.langues_bouton.place(relx=0.60, rely=1, anchor='se')

        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.button_return())
        self.x_button.pack(side="left",padx=(0,5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

        self.annees_cate_bouton = ctk.CTkButton(self, text="Caté/Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees_cate())
        self.annees_cate_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_cate_bouton.place(relx=0.80, rely=1, anchor='se')

    def button_return(self):
        self.master.show_accueil()

    #Ajout des liens pour déployer les nouveaux diagrammes
    def bouton_durees(self):
        self.master.show_stats_durees()

    def bouton_annees(self):
        self.master.show_stats_annees()

    def bouton_langues(self):
        self.master.show_stats_langues()

    def bouton_annees_cate(self):
        self.master.show_stats_cate_annees()