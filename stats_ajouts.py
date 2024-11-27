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
        #print(groupe_langues_court)
        
        self.langues = list(groupe_langues_court.index)
        self.sizes = list(groupe_langues_court.values)

        plt.figure(0)
        plt.pie(self.sizes, labels=self.langues, autopct='%1.1f%%', pctdistance= 0.9)
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
        groupe_annees = groupe_annees_brut.drop(labels="")
        
        self.annees = list(groupe_annees.index)
        self.sizes = list(groupe_annees.values)

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
        #print(groupe_durees_brut)
        
        #Nettoyage d'une ligne sans titre et absente des Recommendations
        groupe_durees = groupe_durees_brut.drop(labels="")
        
        self.durees = list(groupe_durees.index)
        self.sizes = list(groupe_durees.values)

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
