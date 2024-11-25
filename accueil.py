import customtkinter as ctk
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from movie_list_functions import clean_dataframe

file = "movie_list.csv"
df = clean_dataframe(file)

class Accueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        self.configure(width=750, height=850)
        self.pack()
        self.pack_propagate(False)

        #Frame pour les utilisateurs
        self.user_frame = ctk.CTkFrame(self)
        self.user_frame.pack(padx=5,pady=5)
        self.user_frame.place(relx=0.5,rely=0.5,anchor="center")

        #Obtient la position du fichier
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.abspath(".")

        save_folder = os.path.join(base_dir, "userinfo")

        #Creer le dossier s'il n'existe pas
        os.makedirs(save_folder, exist_ok=True)
        
        list = os.listdir(save_folder)

        #Ajouter un titre
        self.main_label = ctk.CTkLabel(self.user_frame, text="Choisissez un Utilisateur")
        self.main_label.pack(padx=8,pady=8)
        
        #Avec la liste d'utilisateurs, retourn leurs noms
        for user in list:

            file_path = os.path.join("userinfo", user)
            
            with open(file_path, 'r') as file:
                
                lines = file.readlines() 

                prenom = lines[0].replace('\n','')
                nom = lines[1].replace('\n','')
                username = prenom + nom
                
                self.button_frame = ctk.CTkFrame(self.user_frame)
                self.button_frame.pack(padx=2,pady=2)

                self.user_button = ctk.CTkButton(self.button_frame, text=prenom, command=lambda:self.button_load(username))
                self.user_button.pack(side="left",padx=5,pady=5)

                self.x_button = ctk.CTkButton(self.button_frame, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.button_delete(username))
                self.x_button.pack(padx=(0,5), side="right",pady=5)

                self.chan_button = ctk.CTkButton(self.button_frame, text="Modi.", width=30, fg_color="blue", hover_color="darkblue", command=lambda : self.button_change(username))
                self.chan_button.pack(padx=(0,5), side="right",pady=5)
                
        self.new_button = ctk.CTkButton(self.user_frame, text="Nouvel Utilisateur", command=self.button_nouv)
        self.new_button.pack(padx=5,pady=5)

        self.stats_button = ctk.CTkButton(self, text="Voir Statistiques", command=self.button_stat)
        self.stats_button.pack(padx=5,pady=5)
        self.stats_button.place(relx=1, rely=1, anchor='se')

    def button_change(self, username):
        self.master.show_changer(username)

    def button_load(self,username):
        self.master.show_recommendations(username)

    def button_nouv(self):
        self.master.show_profil()

    def button_stat(self):
        self.master.show_stats()

    def button_delete(self,username):

        #Obtient la position du fichier
        if getattr(sys, 'frozen', False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.abspath(".")

        save_folder = os.path.join(base_dir, "userinfo")
        
        file_path = os.path.join(save_folder, username+"_userinfo.txt")

        os.remove(file_path)

        self.clear_frame()

        self.create_widgets()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()