import customtkinter as ctk
from movie_list_functions import *
from user import User

file = "movie_list.csv"
df = clean_dataframe(file)

class Recommendations(ctk.CTkFrame):

    def __init__(self, master=None, username=""):
        super().__init__(master)
        self.master = master
        self.user = User(username)
        self.create_widgets()

    def create_widgets(self):

        self.pack()

        #Frame pour les tags
        self.tags_frame = ctk.CTkFrame(self)
        self.tags_frame.pack(fill="x",padx=5,pady=5)

        self.duree_option = ctk.CTkOptionMenu(self.tags_frame, values=get_all_tags("duree"))
        self.duree_option.pack(side="left",padx=5,pady=5)
        self.duree_option.set("Durée")

        self.date_option = ctk.CTkOptionMenu(self.tags_frame, values=get_all_tags("date"))
        self.date_option.pack(side="left",padx=5,pady=5)
        self.date_option.set("Année")

        self.categorie_option = ctk.CTkOptionMenu(self.tags_frame, values=get_all_tags("categorie"))
        self.categorie_option.pack(side="left",padx=5,pady=5)
        self.categorie_option.set("Type")

        self.sous_categorie_option = ctk.CTkOptionMenu(self.tags_frame, values=get_all_tags("sous-categorie"))
        self.sous_categorie_option.pack(side="left",padx=5,pady=5)
        self.sous_categorie_option.set("Catégorie")

        self.langue_option = ctk.CTkOptionMenu(self.tags_frame, values=get_all_tags("langue"))
        self.langue_option.pack(side="left",padx=5,pady=5)
        self.langue_option.set("Langue")

        #Frame pour les recommendations
        self.recs_frame = ctk.CTkFrame(self, height=650)
        self.recs_frame.pack(fill="x", expand=False)
        self.recs_frame.pack_propagate(False)

        self.none_label = ctk.CTkLabel(self.recs_frame, text="Aucun film à recommander...")
        self.none_label.place(relx=0.5, rely=0.5, anchor='center')

        #Frame pour le bouton de recommendation
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(fill="x",padx=5,pady=5)

        self.rec_button = ctk.CTkButton(self.button_frame, text="Recommandes moi des films!", command=self.recommande_films, width=695)
        self.rec_button.pack(side="left",padx=5,pady=5)

        self.x_button = ctk.CTkButton(self.button_frame, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.return_button())
        self.x_button.pack(side="left",padx=(0,5), pady=5)

        self.labels_films = []
        
    def recommande_films(self):

        if self.langue_option.get() != "Langue" and self.categorie_option.get() != "Type" and self.sous_categorie_option.get() != "Catégorie" and self.date_option.get() != "Année" and self.duree_option.get() != "Durée":

            #Supprime les label précédents
            self.none_label.destroy()
            for film_label in self.labels_films:
                film_label.destroy()
            self.labels_films = []

            #Utilise differents masques pour filtrer les films
            masque_langue = df["LANGUE_PRINCIPALE_1017"] == self.langue_option.get()
            masque_categorie = df["CATEGORIE"] == self.categorie_option.get()
            masque_sous_categorie = df["SOUS_CATEGORIE"] == self.sous_categorie_option.get()
            masque_date = df["DATE_PRODUCTION_046K"] == self.date_option.get()
            masque_duree = df["DUREE_CONTENU"] == self.duree_option.get()

            films_filtree = films_recommendee = df[masque_langue][masque_categorie][masque_sous_categorie][masque_date][masque_duree]


            #Donne des ratings aux films
            tags = self.user.tags

            films_filtree["RATING"] = 0

            for i in range(len(films_filtree.index)):
                films_filtree.iloc[i, films_filtree.columns.get_loc('RATING')] = get_movie_rating(i, tags)

            films_filtree = films_filtree.sort_values("RATING", ascending=False)

            print(films_filtree)

            films_recommendee = films_filtree[masque_langue][masque_categorie][masque_sous_categorie][masque_date][masque_duree].head(20)

            #Affiche les recommendations
            for index, row in films_recommendee.iterrows():

                film = row["TITRE_245a"]
                rating  = row["RATING"]

                self.film_frame = ctk.CTkFrame(self.recs_frame)
                self.film_frame.pack(fill="x")

                self.film_label = ctk.CTkLabel(self.film_frame, text=film)
                self.film_label.pack(side="left",padx=50,pady=5)

                self.rating_label = ctk.CTkLabel(self.film_frame, text="Note : "+str(rating))
                self.rating_label.pack(side="right",padx=50,pady=5)

                if film != "":
                    self.labels_films.append(self.film_frame)

            if len(self.labels_films) == 0:
                self.none_label = ctk.CTkLabel(self.recs_frame, text="Aucun film avec ces critères n'a été trouvé!")
                self.none_label.place(relx=0.5, rely=0.5, anchor='center')


    def return_button(self):
        self.master.show_accueil()