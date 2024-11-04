import tkinter as tk
import pandas as pd
from pandastable import Table

# Load data
df = pd.read_csv("extract.csv", encoding="Windows-1252", on_bad_lines='skip', 
                 usecols=['TITRE_245a', 'DUREE_CONTENU', 'PRODUCTION_264B', 
                          'LANGUE_PRINCIPALE_1017', 'CATEGORIE', 
                          'SOUS_CATEGORIE', 'DATE_PRODUCTION_046K'])

class TableEditor:
    def __init__(self):
        # Initialize Tkinter root window
        self.root = tk.Tk()
        self.root.title('Table Editor')

        # Create and pack a frame to hold the table
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill='both', expand=True)

        # Set up the table with the DataFrame
        self.table = Table(self.frame, dataframe=df, showstatusbar=True, showtoolbar=True)
        self.table.show()

        # Run the main loop
        self.root.mainloop()

if __name__ == '__main__':
  TableEditor()
    