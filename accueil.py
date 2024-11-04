import customtkinter as ctk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Accueil(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.button_nouv = ctk.CTkButton(self, text="Nouvel utilisateur", command=self.button_nouv) # Bouton
        self.button_nouv.grid(row=0, column=0, pady=(20,10))

    def button_nouv(self):
        self.master.show_creaProfil()