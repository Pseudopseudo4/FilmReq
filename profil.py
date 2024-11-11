import customtkinter as ctk
from search_algo import *

class Profil(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.pack()
        
        #Frame pour l'information personelle
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(fill="x")

        # Prénom
        self.firstname_label = ctk.CTkLabel(self.info_frame, text="Prénom:")
        self.firstname_label.pack(side="left",padx=5,pady=5)
        self.firstname_entry = ctk.CTkEntry(self.info_frame, placeholder_text="Entrez votre prénom")
        self.firstname_entry.pack(side="left",padx=5,pady=5)

        # Nom
        self.name_label = ctk.CTkLabel(self.info_frame, text="Nom:")
        self.name_label.pack(side="left",padx=5,pady=5)
        self.name_entry = ctk.CTkEntry(self.info_frame, placeholder_text="Entrez votre nom")
        self.name_entry.pack(side="left",padx=5,pady=5)

        # Langue
        languages = get_all_tags("langue")
        self.langue_label = ctk.CTkLabel(self.info_frame, text="Langue:")
        self.langue_label.pack(side="left",padx=5,pady=5)
        
        self.langue_option = ctk.CTkOptionMenu(self.info_frame, values=languages)
        self.langue_option.pack(side="left",padx=5,pady=5)
        self.langue_option.set("Sélectionnez la langue")

        #Frame pour les films
        self.films_frame = ctk.CTkFrame(self,width=750,height=776)
        self.films_frame.pack(fill="x")     
        self.films_frame.pack_propagate(False)

        #Film aimé/non
        self.liked_movies       = UserMoviesList(self, "Films Aimés", 375, "left")
        self.disliked_movies    = UserMoviesList(self, "Films Pas Aimés", 375, "right")

        #Frame pour la sauvegarde ou efface de profil
        self.controle_frame = ctk.CTkFrame(self)
        self.controle_frame.pack(fill="x")

        #Bouton sauvegarde
        self.save_button = ctk.CTkButton(self.controle_frame, text="Sauvegarder", width=30, command=lambda : self.save_user())
        self.save_button.pack(padx=5,pady=5,side="left")

        self.delete_button = ctk.CTkButton(self.controle_frame, text="Annuler", width=30, fg_color="red", hover_color="darkred", command=lambda : self.return_button())
        self.delete_button.pack(padx=5,pady=5,side="right")


    def save_user(self):

        if self.firstname_entry.get() != "" and self.name_entry.get() != "" and self.langue_option.get() != "Sélectionnez la langue":
        
            username = self.firstname_entry.get()+self.name_entry.get()

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
                
                file.write(self.firstname_entry.get()+"\n")
                file.write(self.name_entry.get()+"\n")
                file.write(self.langue_option.get()+"\n")

                for name, id in self.liked_movies.movies:
                    file.write(str(id)+",")
                file.write("\n")

                for name, id in self.disliked_movies.movies:
                    file.write(str(id)+",")
                file.write("\n")

                file.write("\n")
            
            self.master.show_recommendations(username)

    def return_button(self):
        self.master.show_accueil()