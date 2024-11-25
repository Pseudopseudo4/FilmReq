import customtkinter as ctk
from user import User
from search_algo import *


class Changer_ajout(ctk.CTkFrame):
    def __init__(self, master=None, username="", prenom="", nom="", langue="", films_aimes=[], films_pas=[]):#Erreur dans ce fichier
        super().__init__(master)
        self.master = master
        self.user = User(username)
        self.create_widgets()
        self.prenom = prenom
        self.nom = nom
        self.langue = langue
        self.films_aimes = films_aimes
        self.films_pas =films_pas

    def create_widgets(self):
        self.pack()

    #Frame pour les films
        self.films_frame = ctk.CTkFrame(self,width=750,height=776)
        self.films_frame.pack(fill="x")     
        self.films_frame.pack_propagate(False)

        #Film aimé/non
        self.liked_movies       = UserMoviesList(self, "Films Aimés", 350, "left")
        self.disliked_movies    = UserMoviesList(self, "Films Pas Aimés", 350, "right")

        #Frame pour la sauvegarde ou efface de profil
        self.controle_frame = ctk.CTkFrame(self)
        self.controle_frame.pack(fill="x")

        #Bouton sauvegarde
        self.save_button = ctk.CTkButton(self.controle_frame, text="Sauvegarder", width=30, command=lambda : self.save_user())
        self.save_button.pack(padx=5,pady=5,side="left")

        self.delete_button = ctk.CTkButton(self.controle_frame, text="Annuler", width=30, fg_color="red", hover_color="darkred", command=lambda : self.return_button())
        self.delete_button.pack(padx=5,pady=5,side="right")


    def save_user(self):

        if self.prenom != "" and self.nom!= "" and self.langue != "Sélectionnez la langue":
        
            username = self.prenom+self.nom

            #Obtient la position du fichier
            if getattr(sys, 'frozen', False):
                base_dir = os.path.dirname(sys.executable)
            else:
                base_dir = os.path.abspath(".")

            save_folder = os.path.join(base_dir, "userinfo")

            #Creer le dossier s'il n'existe pas
            os.makedirs(save_folder, exist_ok=True)

            file_path = os.path.join(save_folder, username+"_userinfo.txt")

            #Sauvegarder vers un fichier l'info d'utilisateur
            with open(file_path, "w") as file:
                
                file.write(self.prenom+"\n")
                file.write(self.nom+"\n")
                file.write(self.langue+"\n")

                #Mise à jour des films aimés déjà enregistrés
                for entree in self.films_aimes:
                    file.write(str(entree)+",")

                for name, id in self.liked_movies.movies:
                    file.write(str(id)+",")
                file.write("\n")

                #Mise à jour des films pas déjà enregistrés
                for entree in self.films_pas:
                    file.write(str(entree)+",")
                    
                for name, id in self.disliked_movies.movies:
                    file.write(str(id)+",")
                file.write("\n")

                file.write("\n")
            
            self.master.show_recommendations(username)

    def return_button(self):
        self.master.show_accueil()

        