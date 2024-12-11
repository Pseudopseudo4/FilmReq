import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from movie_list_functions import clean_dataframe

file = "movie_list.csv"
df = clean_dataframe(file)

class Stats_langues(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Frame pour le diagramme
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5,pady=5)
        self.stat_frame.place(relx=0.5,rely=0.5,anchor="center")

        #Prise des données pour les langues du fichier
        groupe_langues = df.groupby('LANGUE_PRINCIPALE_1017').size().sort_values(ascending=False)
        
        #réduction à un échantillon, pour la lisibilité, selon la valeur
        groupe_langues_court = groupe_langues[groupe_langues.values > 100]
        
        self.langues = list(groupe_langues_court.index)
        self.sizes = list(groupe_langues_court.values)

        plt.close(fig=0)
        plt.figure(0)
        plt.bar(self.langues, self.sizes, width=0.5)
        plt.title("Distribution des langues")

        # Intégrer le graphique
        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.stat_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.durees_bouton = ctk.CTkButton(self, text="Durées", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_durees())
        self.durees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.durees_bouton.place(relx=0.40, rely=1, anchor='se')

        self.annees_bouton = ctk.CTkButton(self, text="Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees())
        self.annees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_bouton.place(relx=0.50, rely=1, anchor='se')

        self.categories_bouton = ctk.CTkButton(self, text="Catégories", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_categories())
        self.categories_bouton.pack(side="left",padx=(0,5), pady=5)
        self.categories_bouton.place(relx=0.60, rely=1, anchor='se')
        
        self.annees_cate_bouton = ctk.CTkButton(self, text="Caté/Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees_cate())
        self.annees_cate_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_cate_bouton.place(relx=0.80, rely=1, anchor='se')

        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.bouton_retour())
        self.x_button.pack(side="left",padx=(0,5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

    def bouton_retour(self):
        self.master.show_accueil()

    def bouton_categories(self):
        self.master.show_stats()

    def bouton_annees(self):
        self.master.show_stats_annees()

    def bouton_durees(self):
        self.master.show_stats_durees()
    
    def bouton_annees_cate(self):
        self.master.show_stats_cate_annees()

class Stats_annees(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Frame pour le diagramme
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5,pady=5)
        self.stat_frame.place(relx=0.5,rely=0.5,anchor="center")


        #Prise des données pour les années du fichier
        groupe_annees_brut = df.groupby('DATE_PRODUCTION_046K').size()

        #Nettoyage de lignes absentes de la sélection dans les Recommendations
        groupe_annees = groupe_annees_brut.drop(labels="2020-2030")
        groupe_annees = groupe_annees.drop(labels="")
        
        self.annees = list(groupe_annees.index)
        self.sizes = list(groupe_annees.values)

        plt.close(fig=3)
        plt.figure(3)
        plt.pie(self.sizes, labels=self.annees, autopct='%1.1f%%', pctdistance=0.75)
        plt.title("Distribution des années")

        # Intégrer le graphique
        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.stat_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.durees_bouton = ctk.CTkButton(self, text="Durées", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_durees())
        self.durees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.durees_bouton.place(relx=0.40, rely=1, anchor='se')

        self.catégories_bouton = ctk.CTkButton(self, text="Catégories", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_categories())
        self.catégories_bouton.pack(side="left",padx=(0,5), pady=5)
        self.catégories_bouton.place(relx=0.50, rely=1, anchor='se')

        self.langues_bouton = ctk.CTkButton(self, text="Langues", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_langues())
        self.langues_bouton.pack(side="left",padx=(0,5), pady=5)
        self.langues_bouton.place(relx=0.60, rely=1, anchor='se')

        self.annees_cate_bouton = ctk.CTkButton(self, text="Caté/Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees_cate())
        self.annees_cate_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_cate_bouton.place(relx=0.80, rely=1, anchor='se')

        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.bouton_retour())
        self.x_button.pack(side="left",padx=(0,5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

    def bouton_retour(self):
        self.master.show_accueil()

    def bouton_categories(self):
        self.master.show_stats()

    def bouton_langues(self):
        self.master.show_stats_langues()

    def bouton_durees(self):
        self.master.show_stats_durees()

    def bouton_annees_cate(self):
        self.master.show_stats_cate_annees()  

class Stats_durees(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Frame pour le diagramme
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5,pady=5)
        self.stat_frame.place(relx=0.5,rely=0.5,anchor="center")

        #Prise des données pour les durées du fichier
        groupe_durees_brut = df.groupby('DUREE_CONTENU').size().sort_values(ascending=False)
        
        #Nettoyage d'une ligne sans titre et absente des Recommendations
        groupe_durees = groupe_durees_brut.drop(labels="")
        
        self.durees = list(groupe_durees.index)
        self.sizes = list(groupe_durees.values)

        plt.close(fig=4)
        plt.figure(4)
        plt.pie(self.sizes, labels=self.durees, autopct='%1.1f%%')
        plt.title("Distribution des durées")

        # Intégrer le graphique
        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.stat_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.categories_bouton = ctk.CTkButton(self, text="Catégories", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_categories())
        self.categories_bouton.pack(side="left",padx=(0,5), pady=5)
        self.categories_bouton.place(relx=0.40, rely=1, anchor='se')

        self.annees_bouton = ctk.CTkButton(self, text="Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees())
        self.annees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_bouton.place(relx=0.50, rely=1, anchor='se')

        self.langues_bouton = ctk.CTkButton(self, text="Langues", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_langues())
        self.langues_bouton.pack(side="left",padx=(0,5), pady=5)
        self.langues_bouton.place(relx=0.60, rely=1, anchor='se')

        self.annees_cate_bouton = ctk.CTkButton(self, text="Caté/Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees_cate())
        self.annees_cate_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_cate_bouton.place(relx=0.80, rely=1, anchor='se')

        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.bouton_retour())
        self.x_button.pack(side="left",padx=(0,5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

    def bouton_retour(self):
        self.master.show_accueil()

    def bouton_categories(self):
        self.master.show_stats()

    def bouton_langues(self):
        self.master.show_stats_langues()

    def bouton_annees(self):
        self.master.show_stats_annees()
    
    def bouton_annees_cate(self):
        self.master.show_stats_cate_annees()

class Stats_annees_cate(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        

    def create_widgets(self):
        
        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Prise des données pour les années du fichier
        groupe_annees_brut = df.groupby('DATE_PRODUCTION_046K').size()

        #Nettoyage de lignes absentes de la sélection dans les Recommendations
        groupe_annees = groupe_annees_brut.drop(labels="2020-2030")
        groupe_annees = groupe_annees.drop(labels="")

        self.annees = list(groupe_annees.index)

        #Prise des données pour les catégories du fichier
        groupe_annees_cate = df.groupby(['DATE_PRODUCTION_046K','CATEGORIE']).size()

        groupe_annees_cate = groupe_annees_cate.drop(labels="")
        groupe_annees_cate = groupe_annees_cate.drop(labels="2020-2030")

        
        listes_cate_ind =[]
        #Dictionnaire avec clé = Catégories et valeurs = liste des périodes d'Années pour obtenir l'axe y de chaque instance de graphique
        dico_cate_annees = groupe_annees_cate.index.get_level_values(level=0).groupby(groupe_annees_cate.index.get_level_values(level=1))
        for cate in dico_cate_annees:
            liste_temp = []
            for date in dico_cate_annees[cate]:
                liste_temp.append(groupe_annees_cate.loc[(date,cate)])
            listes_cate_ind.append(liste_temp)

        #Frame pour les diagramme Catégories/années et Sous-catégories/années
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5,pady=5)
        self.stat_frame.place(relx=0.5,rely=0.5,anchor="center")

        #S'assurer que le graphique ne se dédouble pas
        plt.close(fig=5)
        #Données pour les Catégories selon les segments d'Années
        plt.figure(5, figsize=(7,4))
        plt.plot(self.annees, listes_cate_ind[0], label="Documentaire")
        plt.plot(self.annees, listes_cate_ind[1], label="Fiction")
        plt.plot(self.annees, listes_cate_ind[2], label="N.A")
        plt.plot(self.annees, listes_cate_ind[3], label="Série télévisée")
        plt.legend(loc="upper left")
        plt.title("Distribution des catégories par année")
        plt.xticks(rotation=45, ha='right')
        
        # Intégrer le graphique
        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.stat_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
        
        #Prise des données pour les sous-catégories du fichier
        groupe_annees_sousCate = df.groupby(['DATE_PRODUCTION_046K','SOUS_CATEGORIE']).size()

        groupe_annees_sousCate = groupe_annees_sousCate.drop(labels="")
        groupe_annees_sousCate = groupe_annees_sousCate.drop(labels="2020-2030")

        
        listes_sousCate_ind =[]
        #Dictionnaire avec clé = Sous-catégories et valeurs = liste des périodes d'Années pour obtenir l'axe y de chaque instance de graphique
        dico_sousCate_annees = groupe_annees_sousCate.index.get_level_values(level=0).groupby(groupe_annees_sousCate.index.get_level_values(level=1))
        for cate in dico_sousCate_annees:
            liste_temp = []
            for date in dico_sousCate_annees[cate]:
                liste_temp.append(groupe_annees_sousCate.loc[(date,cate)])
            listes_sousCate_ind.append(liste_temp)

        #S'assurer que le graphique ne se dédouble pas
        plt.close(fig=6)

        plt.figure(6, figsize=(7,4))
        #Graphiques seulement pour les sous-catégories représentées dans le graphique circulaire, à l'exception de Other (Autre)
        plt.plot(self.annees, listes_sousCate_ind[0], label="Action")
        plt.plot(self.annees, listes_sousCate_ind[5], label="Comédie")
        plt.plot(self.annees, listes_sousCate_ind[6], label="Drame")
        plt.plot(self.annees, listes_sousCate_ind[7], label="Fantastique")
        plt.plot(self.annees, listes_sousCate_ind[12], label="Musique")
        plt.plot(self.annees, listes_sousCate_ind[16], label="Policier")
        plt.legend(loc="upper left")
        plt.title("Distribution des sous-catégories principales par année")
        plt.xticks(rotation=45, ha='right')
        

        # Intégrer le graphique
        self.canvas = FigureCanvasTkAgg(plt.gcf(), self.stat_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        

        self.durees_bouton = ctk.CTkButton(self, text="Durées", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_durees())
        self.durees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.durees_bouton.place(relx=0.40, rely=1, anchor='se')

        self.catégories_bouton = ctk.CTkButton(self, text="Catégories", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_categories())
        self.catégories_bouton.pack(side="left",padx=(0,5), pady=5)
        self.catégories_bouton.place(relx=0.80, rely=1, anchor='se')

        self.langues_bouton = ctk.CTkButton(self, text="Langues", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_langues())
        self.langues_bouton.pack(side="left",padx=(0,5), pady=5)
        self.langues_bouton.place(relx=0.60, rely=1, anchor='se')

        self.annees_bouton = ctk.CTkButton(self, text="Années", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.bouton_annees())
        self.annees_bouton.pack(side="left",padx=(0,5), pady=5)
        self.annees_bouton.place(relx=0.50, rely=1, anchor='se')

        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.bouton_retour())
        self.x_button.pack(side="left",padx=(0,5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

        

    def bouton_retour(self):
        self.master.show_accueil()

    def bouton_categories(self):
        self.master.show_stats()

    def bouton_langues(self):
        self.master.show_stats_langues()
        
    def bouton_annees(self):
        self.master.show_stats_annees()

    def bouton_durees(self):
        self.master.show_stats_durees()