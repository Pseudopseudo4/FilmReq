import customtkinter as ctk
import tkinter as tk
import pandas as pd
import os
from pandastable import Table
from searchAlgo import *
from user import *

class ReqPage(ctk.CTkFrame):

    def __init__(self, parent):

        #Frame pour la page complete
        self.main_frame = ctk.CTkFrame(parent)
        self.main_frame.pack()

        duree = 100
        categorie = "FICTION"
        annee = 1980
        langue = "anglais"

        df = cleanMovies()
        df = df[df["CATEGORIE"] == categorie]
        df = df[df["LANGUE_PRINCIPALE_1017"] == langue]

        tags = User("LaurnetPe").tags

        df["RATING"] = 0

        for i in range(len(df.index)):
            df.iloc[i, df.columns.get_loc('RATING')] = get_movie_rating(i, tags)

        df = df.sort_values("RATING", ascending=False)

        print(df.head(10))
        