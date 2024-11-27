import customtkinter as ctk
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from movie_list_functions import clean_dataframe

file = "movie_list.csv"
df = clean_dataframe(file)

class Stats(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.configure(width=750, height=750)
        self.pack()
        self.pack_propagate(False)

        # Frame for the pie charts
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5, pady=5)
        self.stat_frame.place(relx=0.5, rely=0.5, anchor="center")

        if 'CATEGORIE' in df.columns:

            category_counts = df['CATEGORIE'].value_counts(normalize=True) * 100
            threshold = 2
            major_categories = category_counts[category_counts >= threshold]
            minor_categories = category_counts[category_counts < threshold].sum()


            if minor_categories > 0:
                major_categories['Other'] = minor_categories


            fig, ax = plt.subplots(figsize=(4, 4))
            ax.pie(major_categories, labels=major_categories.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Distribution des catégories")


            canvas = FigureCanvasTkAgg(fig, self.stat_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        if 'SOUS_CATEGORIE' in df.columns:

            category_counts = df['SOUS_CATEGORIE'].value_counts(normalize=True) * 100
            threshold = 4
            major_categories = category_counts[category_counts >= threshold]
            minor_categories = category_counts[category_counts < threshold].sum()


            if minor_categories > 0:
                major_categories['Other'] = minor_categories


            fig, ax = plt.subplots(figsize=(4, 4))
            ax.pie(major_categories, labels=major_categories.index, autopct='%1.1f%%', startangle=140)
            ax.set_title("Distribution des sous-catégories")

            canvas = FigureCanvasTkAgg(fig, self.stat_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        # Button to switch to create_widgets2
        self.switch_button = ctk.CTkButton(self, text="Montre plus de stats", command=self.switch_to_widgets2)
        self.switch_button.pack(pady=10)


        self.x_button = ctk.CTkButton(self, text="X", width=30, fg_color="red", hover_color="darkred",
                                      command=lambda: self.button_return())
        self.x_button.pack(side="left", padx=(0, 5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

    def create_widgets2(self):
        print("Switching to create_widgets2...")
        
        for widget in self.winfo_children():
            widget.destroy()

        self.configure(width=750, height=750)
        self.pack()
        self.pack_propagate(False)

        # Create a new stat_frame
        self.stat_frame = ctk.CTkFrame(self)
        self.stat_frame.pack(padx=5, pady=5)
        self.stat_frame.place(relx=0.5, rely=0.5, anchor="center")

        def process_user_files():
            
            if getattr(sys, 'frozen', False):
                base_dir = os.path.dirname(sys.executable)
            else:
                base_dir = os.path.abspath(".")

            save_folder = os.path.join(base_dir, "userinfo")
            os.makedirs(save_folder, exist_ok=True)  

            liked_categories = []
            disliked_categories = []

            
            for user_file in os.listdir(save_folder):
                file_path = os.path.join(save_folder, user_file)

                
                with open(file_path, 'r') as file:
                    lines = file.readlines()

                    if len(lines) >= 5:  
                        liked_ids = [int(x) for x in lines[3].strip().split(',') if x.isdigit()]
                        disliked_ids = [int(x) for x in lines[4].strip().split(',') if x.isdigit()]

                        
                        liked_categories.extend(df.loc[df.index.isin(liked_ids), 'CATEGORIE'].tolist())
                        disliked_categories.extend(df.loc[df.index.isin(disliked_ids), 'CATEGORIE'].tolist())

            return liked_categories, disliked_categories



        
        liked_categories, disliked_categories = process_user_files()

        #print(f"Liked categories: {liked_categories}")
        #print(f"Disliked categories: {disliked_categories}")

        
        if liked_categories:
            liked_counts = pd.Series(liked_categories).value_counts(normalize=True) * 100
            liked_major = liked_counts[liked_counts >= 2]
            liked_minor = liked_counts[liked_counts < 2].sum()
            if liked_minor > 0:
                liked_major["Other"] = liked_minor

            fig_liked, ax_liked = plt.subplots(figsize=(4, 4))
            ax_liked.pie(liked_major, labels=liked_major.index, autopct='%1.1f%%', startangle=140)
            ax_liked.set_title("Catégories de films les plus aimés")

            canvas_liked = FigureCanvasTkAgg(fig_liked, self.stat_frame)
            canvas_liked.draw()
            canvas_liked.get_tk_widget().pack()

        
        if disliked_categories:
            disliked_counts = pd.Series(disliked_categories).value_counts(normalize=True) * 100
            disliked_major = disliked_counts[disliked_counts >= 2]
            disliked_minor = disliked_counts[disliked_counts < 2].sum()
            if disliked_minor > 0:
                disliked_major["Other"] = disliked_minor

            fig_disliked, ax_disliked = plt.subplots(figsize=(4, 4))
            ax_disliked.pie(disliked_major, labels=disliked_major.index, autopct='%1.1f%%', startangle=140)
            ax_disliked.set_title("Catégories de films les moins aimés")

            canvas_disliked = FigureCanvasTkAgg(fig_disliked, self.stat_frame)
            canvas_disliked.draw()
            canvas_disliked.get_tk_widget().pack()

        
        self.x_button = ctk.CTkButton(
            self, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda: self.button_return())
        self.x_button.pack(side="left", padx=(0, 5), pady=5)
        self.x_button.place(relx=1, rely=1, anchor='se')

    def switch_to_widgets2(self):
        self.create_widgets2()

    def button_return(self):
        self.master.show_accueil()