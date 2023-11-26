import tkinter as tk
from tkinter import ttk
from functions.search import search
from config import COLUMNS_IN_SEARCH, WIDTHS_IN_SEARCH

# print('0. Housing ID') id
# print('1. Housing name') name
# print('2. Housing host') host_name
# print('3. Neighborhood') neighbourhood
# print('4. Price') price
# print('5. Minimum Nights') minimum_nights

class WindowSearch(tk.Toplevel):
    def __init__(self, parent, df, update_df):
        super().__init__(parent)
        self.df = df
        self.update_df = update_df
        self.query = tk.StringVar()
        self.selected_searchby = tk.StringVar()

        self.geometry('320x320')
        self.title('Search')
        tk.Label(self, text='Search', font=('Montserrat Medium', 16)).pack(side=tk.TOP, pady=16)
        
        # Entries
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        label_query = ttk.Label(frame, text='Query')
        label_searchby = ttk.Label(frame, text='Search by')

        entry_query = ttk.Entry(frame, textvariable=self.query)
        cbox_searchby = ttk.Combobox(frame, textvariable=self.selected_searchby)
        cbox_searchby['values'] = ['id', 'price', 'minimum_nights', 'name', 'neighbourhood', 'host_name']
        cbox_searchby['state'] = 'readonly'
        cbox_searchby.set('name')

        label_query.grid(row=0, column = 0, padx=10, pady= 10, sticky='se')
        label_searchby.grid(row=1, column = 0, padx=10, pady=10, sticky='ne')

        entry_query.grid(row=0, column=1, padx=10, pady=10, sticky='sw')
        cbox_searchby.grid(row=1, column=1, padx=10, pady=10, sticky='nw')

        frame.pack(fill=tk.BOTH, expand=True, anchor='center')

        ttk.Button(self,
                text='OK',
                command=self.func_ok).pack(side=tk.LEFT, expand=True, pady=32)

        ttk.Button(self,
                text='Cancel',
                command=self.destroy).pack(side=tk.LEFT, expand=True, pady=32)
    
    def func_ok(self):
        self.df = search(self.df, self.query.get(), self.selected_searchby.get())
        self.update_df(self.df, COLUMNS_IN_SEARCH, WIDTHS_IN_SEARCH)
        self.destroy()