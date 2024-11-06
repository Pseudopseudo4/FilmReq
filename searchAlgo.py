import pandas as pd
import customtkinter as ctk
import tkinter as tk
import csv
from csv import DictReader
from cleanMovies import *
from CTkListbox import *

file = 'extract.csv'
df = cleanMovies()

def searchByTitle(title_name):
    """
    Search movie or show by name and return the matching titles
    """

    with open(file, newline='') as csvfile:

        #Set dataframe as dictionary
        titles      = df["TITRE_245a"].to_dict()

        #Return array
        r = []

        #Check every row
        for row in titles:    
            #If the entered search is present in title, return it
            if matchTitle(title_name, titles[row]):
                r.append([titles[row],row])

            #Only show the first top 20 results
            if len(r) >= 20:
                break

        return r

def matchTitle(searched_title, compared_title):
    """
    Defines the necessary criteria to be met when checking if search corresponds to value
    """
    
    #Create list of every word in search
    words = searched_title.split(" ")

    #Check to see if every word is in the title
    for i in range(len(words)):
        if words[i].lower() not in compared_title.lower():
            return False
    return True

def searchTag(tag_name):
    """
    Search tag by name
    """

def get_entry_position(entry_name):
    return df.index[df["TITRE_245a"] == entry_name].to_list()[0]

class UserMoviesList(ctk.CTkFrame):
    """
    Creates a search bar that returns potential matches of movies in database
    """
    def __init__(self, parent, title, width, alignement):

        self.width = width

        #Create a frame to hold the movies
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(side=alignement,anchor="n",padx=5,pady=5)

        #Add the title label
        self.title = ctk.CTkLabel(self.frame,text=title)
        self.title.pack(pady=(5,0),side="top")

        #Array to store the movie entry ctkinter elements
        self.movie_entries = []

        #Array to store the movie entries to later save
        self.movies = []

        #Create frame to hold the search and match bar
        self.search_frame = ctk.CTkFrame(self.frame)
        self.search_frame.pack(padx=5,pady=5,fill="x",side='bottom')

        #Search bar
        self.entry = ctk.CTkEntry(self.search_frame, width=self.width)
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.on_text_change)  # Bind to key release to update suggestions

        #Match box
        self.matchesbox = CTkListbox(self.search_frame, command=self.on_match_select, width=self.width-35, height=90)
        self.matchesbox.pack_forget()

    def on_text_change(self, event):
        """
        Updates the search results when the searched text changes
        """

        input_text = self.entry.get()
        matches = searchByTitle(input_text)
        self.matchesbox.delete(0, ctk.END)

        #Return the matches in the box
        for match in matches:
            self.matchesbox.insert(ctk.END, match[0])

        if matches:
            self.matchesbox.pack(padx=5,pady=5)
        else:
            self.matchesbox.pack_forget()

    def on_match_select(self, event):
        """
        When a match is selected, add the selection to the movie list
        """

        # Insert selected suggestion into the entry field
        selection = self.matchesbox.get()
        self.entry.delete(0, ctk.END)
        self.matchesbox.delete(0, ctk.END)
        self.matchesbox.pack_forget()

        #Add to the entries
        self.add_entry(selection)

    def add_entry(self, name):
        """
        Adds a movie entry (name & ID) to the movie list
        """

        #Frame to hold the movie
        self.title_frame = ctk.CTkFrame(self.frame)
        self.title_frame.pack(padx=5,pady=5,fill="x")
        
        #Movie title
        self.label = ctk.CTkEntry(self.title_frame, width=self.width-35)
        self.label.insert(0, name)
        self.label.configure(state="disabled")
        self.label.pack(side="left")

        #Create Button to remove movie
        entry_id = self.title_frame
        self.x_button = ctk.CTkButton(self.title_frame, text="X", width=30, fg_color="red", hover_color="darkred", command=lambda : self.delete_entry(entry_id))
        self.x_button.pack(padx=(5,0), side="right")

        #Add the entry to an array for access
        self.movie_entries.append(self.title_frame)
        self.movies.append([name, get_entry_position(name)])

    def delete_entry(self, entry):
        """
        Removes a movie entry from the list with the entry's ID
        """
        
        #Delete the entry
        entry.pack_forget()

        #Remove entry from array
        for i in range(len(self.movie_entries)):
            if self.movie_entries[i] == entry:
                self.movie_entries.pop(i)
                break