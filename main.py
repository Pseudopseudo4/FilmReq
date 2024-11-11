import customtkinter as ctk
from accueil import Accueil
from profil import Profil
from recommendations import Recommendations
from stats import Stats

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

    def show_recommendations(self,username):
        self.clear_main_frame()
        self.recommendations = Recommendations(self,username)

    def show_stats(self):
        self.clear_main_frame()
        self.stats = Stats(self)

    def clear_main_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
