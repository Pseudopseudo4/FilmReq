import customtkinter as ctk
import tkinter as tk

from searchAlgo import *

class UserPage(ctk.CTk):

    def __init__(self, parent):
        
        #Create a frame to hold the liked and disliked movies
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack()

        self.liked_movies       = UserMoviesList(self.frame, "Films Aimés", 300, "left")
        self.disliked_movies    = UserMoviesList(self.frame, "Films Pas Aimés", 300, "right")