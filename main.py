import customtkinter as ctk
from accueil import Accueil
from profil import Profil
from recommendations import Recommendations
from stats import Stats
from changer import Changer
from changer_ajout import Changer_ajout
from stats_ajouts import Stats_annees, Stats_durees, Stats_langues

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("750x850")
        self.title("Application de recommendation de film")
        self.resizable(width=False, height=False)

        self.show_accueil()

    def show_accueil(self):
        self.clear_main_frame()
        self.accueil = Accueil(self)

    def show_profil(self):
        self.clear_main_frame()
        self.profil = Profil(self)

    def show_changer(self, username):
        self.clear_main_frame()
        self.changer = Changer(self,username)

    def show_changer_ajout(self, username, prenom, nom, langue, films_aimes, films_pas):
        self.clear_main_frame()
        self.changer = Changer_ajout(self,username, prenom, nom, langue, films_aimes, films_pas)

    def show_recommendations(self,username):
        self.clear_main_frame()
        self.recommendations = Recommendations(self,username)      
   
    def show_stats(self):   #Statistiques pour les catégories/sous-catégories
        self.clear_main_frame()
        self.stats = Stats(self)

    def show_stats_langues(self):   
        self.clear_main_frame()
        self.stats = Stats_langues(self)

    def show_stats_annees(self):   
        self.clear_main_frame()
        self.stats = Stats_annees(self)

    def show_stats_durees(self):   
        self.clear_main_frame()
        self.stats = Stats_durees(self)

    def clear_main_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
