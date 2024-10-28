import customtkinter as ctk
import tkinter as tk

class User(ctk.CTkFrame):
    def __init__(self, master=None, nom=None, langue=None):
        super().__init__(master)
        self.nom = nom
        self.langue = langue
        
