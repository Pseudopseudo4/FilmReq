import customtkinter as ctk
from user import User
from search_algo import *


class Changer(ctk.CTkFrame):

    def __init__(self, master=None, username=""):
        super().__init__(master)
        self.master = master
        self.user = User(username)
        self.create_widgets()
        self.username = username

    def create_widgets(self):
        self.pack()

        #Frame pour l'information personelle
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(fill="x")

        
        #Create a frame to hold the movies
        self.frame_aimes = ctk.CTkFrame(self)
        self.frame_aimes.pack(side="left",anchor="n",padx=5,pady=5)

        self.frame_pas_aimes = ctk.CTkFrame(self)
        self.frame_pas_aimes.pack(side="right",anchor="n",padx=5,pady=5)

        #Array to store the movie entry ctkinter elements
        self.movie_entries_aimes = []
        self.movie_entries_pas = []

        # Obtenir le prénom du fichier
        self.prenom = self.user.prenom
        # Nouveau prénom
        self.firstname_label = ctk.CTkLabel(self.info_frame, text="Prénom:")
        self.firstname_label.pack(side="left",padx=5,pady=5)
        self.firstname_entry = ctk.CTkEntry(self.info_frame, placeholder_text=self.prenom+" (à réécrire)")
        self.firstname_entry.pack(side="left",padx=5,pady=5)

        # Obtenir le nom du fichier
        self.nom = self.user.nom
        # nouveau Nom
        self.name_label = ctk.CTkLabel(self.info_frame, text="Nom:")
        self.name_label.pack(side="left",padx=5,pady=5)
        self.name_entry = ctk.CTkEntry(self.info_frame, placeholder_text=self.nom+" (à réécrire)")
        self.name_entry.pack(side="left",padx=5,pady=5)

        # Langue
        languages = get_all_tags("langue")
        self.langue_label = ctk.CTkLabel(self.info_frame, text="Langue:")
        self.langue_label.pack(side="left",padx=5,pady=5)
        
        self.langue_option = ctk.CTkOptionMenu(self.info_frame, values=languages)
        self.langue_option.pack(side="left",padx=5,pady=5)
        self.langue_option.set("Sélectionnez la langue")

        #Frame pour les films
        self.films_frame = ctk.CTkFrame(self,width=750,height=700)
        self.films_frame.pack(fill="x")     
        self.films_frame.pack_propagate(False)

        # Obtenir les films aimés/non du fichier
        self.films_aimes = self.user.films_aime
        self.films_pas_aimes = self.user.film_aime_pas
        #print(df)

        for id in self.films_aimes:
            # Ajout à movie_entries_aimes
            self.movie_entries_aimes.append(df.index[df["TITRE_245a"] == df["TITRE_245a"][id]].to_list()[0])

            #Frame to hold the movie
            self.title_frame = ctk.CTkFrame(self.frame_aimes)
            self.title_frame.pack(padx=5,pady=5,fill="x")
            
            #Movie title
            self.label = ctk.CTkEntry(self.title_frame, width=250)
            self.label.insert(0, df["TITRE_245a"][id])
            self.label.configure(state="disabled")
            self.label.pack(side="left")

            #Create Button to remove movie
            entry_id = self.title_frame
            self.x_button = ctk.CTkButton(self.title_frame, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda entry=entry_id, id=id: self.delete_entry("aimes",entry, id))
            self.x_button.pack(padx=(5,0), side="right")

        print("")

        for id in self.films_pas_aimes:
            
            # Ajout à movies_entries_pas
            self.movie_entries_pas.append(df.index[df["TITRE_245a"] == df["TITRE_245a"][id]].to_list()[0])

            #Frame to hold the movie
            self.title_frame = ctk.CTkFrame(self.frame_pas_aimes)
            self.title_frame.pack(padx=5,pady=5,fill="x")
            
            #Movie title
            self.label = ctk.CTkEntry(self.title_frame, width=250)
            self.label.insert(0, df["TITRE_245a"][id])
            self.label.configure(state="disabled")
            self.label.pack(side="left")

            #Create Button to remove movie
            entry_id = self.title_frame
            self.x_button = ctk.CTkButton(self.title_frame, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda entry=entry_id, id=id: self.delete_entry("pas",entry, id))
            self.x_button.pack(padx=(5,0), side="right")

        #Frame pour la sauvegarde ou efface de profil
        self.controle_frame = ctk.CTkFrame(self)
        self.controle_frame.pack(fill="x")

        #Bouton sauvegarde
        self.save_button = ctk.CTkButton(self.controle_frame, text="Sauvegarder", width=30, command=lambda : self.save_user())
        self.save_button.pack(padx=5,pady=5,side="bottom")

        self.delete_button = ctk.CTkButton(self.controle_frame, text="Annuler", width=30, fg_color="red", hover_color="darkred", command=lambda : self.return_button())
        self.delete_button.pack(padx=5,pady=5,side="bottom")

    def return_button(self):
        self.master.show_accueil()

    def delete_entry(self, categorie, entry,id):
        """
        Removes a movie entry from the list with the entry's ID
        """
        
        print("suppression de ",id)
        print("suppression sssde ",entry)
        #Delete the entry
        entry.pack_forget()

        #Remove entry from array
        #Selon la liste aimes/pas
        if categorie == "aimes":
            for i in range(len(self.movie_entries_aimes)):
                if self.movie_entries_aimes[i] == id:
                    self.movie_entries_aimes.pop(i)
                    break

        if categorie == "pas":
            for i in range(len(self.movie_entries_pas)):
                if self.movie_entries_pas[i] == id:
                    self.movie_entries_pas.pop(i)
                    break
        
    def save_user(self):
        if self.firstname_entry.get() != "" and self.name_entry.get() != "" and self.langue_option.get() != "Sélectionnez la langue":
            self.master.show_changer_ajout(self.username, self.firstname_entry.get(), self.name_entry.get(), self.langue_option.get(), self.movie_entries_aimes, self.movie_entries_pas)