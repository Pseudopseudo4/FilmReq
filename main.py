import customtkinter as ctk
import tkinter as tk
import numpy as np
from accueil import Accueil
from user import User

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x850")
        self.title("Appication de recherche")

        self.show_accueil()

    def show_accueil(self):
        self.clear_main_frame()
        self.accueil = Accueil(master=self)

    def show_creaProfil(self):
        self.clear_main_frame()
        self.accueil = User(master=self)

    def clear_main_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()