import tkinter as tk
from tkinter import ttk


class WindowHelp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('800x640')
        self.title('Help')
        tk.Label(self, text='Help', font=('Montserrat Medium', 16)).pack(side=tk.TOP, pady=16)
        

        text = tk.Text(self)
        text.insert('1.0', 
        """
        1. Show 
          This function is used to display housing in order. sorting can 
          be done by id, name, host name, price, and availability 
          for a year.
          
        2. Search
          This function is used to search for lodging based on 
          id, name, host, neighborhood, price, and minimum nights. 
          It will display all housing that matches the search.
          
        3. Add 
          This function is used to add new housing data to the database. 
          It will ask for important data that must be added, 
          such as housing name, host id, host name, etc.
          
        4. Update 
          This function is used to update housing data in the database. 
          It will ask if you want to update the data. 
          Press 'y' for yes and 'n' for no.
          
        5. Delete 
          This function is used to delete housing data in the database. 
          It will ask which housing ID that want to be deleted.
        """)

        text['state'] = 'disabled'
        text.pack(side=tk.TOP, expand=True, fill=tk.BOTH, pady=16)

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(side=tk.TOP, expand=True, pady=16)