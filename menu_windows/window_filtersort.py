import tkinter as tk
from tkinter import ttk
from functions.show import get_filtered
from config import COLUMNS_IN_SHOW, WIDTHS_IN_SHOW

class WindowFilterSort(tk.Toplevel):
    def __init__(self, parent, df, update_df):
        super().__init__(parent)
        self.df = df
        self.update_df = update_df
        self.selected_orderby = tk.StringVar()
        self.selected_order = tk.StringVar()

        self.geometry('320x320')
        self.title('Sort')
        tk.Label(self, text='Sort', font=('Montserrat Medium', 16)).pack(side=tk.TOP, pady=16)
        
        # Entries
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        label_orderby = ttk.Label(frame, text='Sort by')
        label_order = ttk.Label(frame, text='Order')

        cbox_orderby = ttk.Combobox(frame, textvariable=self.selected_orderby)
        cbox_orderby['values'] = ['name', 'neighbourhood']
        cbox_orderby['state'] = 'readonly'
        cbox_orderby.set('name')

        cbox_order = ttk.Combobox(frame, textvariable=self.selected_order)
        cbox_order['values'] = ['Ascending', 'Descending']
        cbox_order['state'] = 'readonly'
        cbox_order.set('Ascending')

        label_orderby.grid(row=1, column=0, padx=10, pady=10, sticky='se')
        label_order.grid(row=2, column=0, padx=10, pady=10, sticky='ne')

        cbox_orderby.grid(row=1, column=1, padx=10, pady=10, sticky='sw')
        cbox_order.grid(row=2, column=1, padx=10, pady=10, sticky='nw')

        frame.pack(fill=tk.BOTH, expand=True, anchor='center')

        ttk.Button(self,
                text='OK',
                command=self.func_ok).pack(side=tk.LEFT, expand=True, pady=32)

        ttk.Button(self,
                text='Cancel',
                command=self.destroy).pack(side=tk.LEFT, expand=True, pady=32)
    
    def func_ok(self):
        self.df = get_filtered(self.df, self.selected_orderby.get(), self.selected_order.get() == 'Ascending')
        self.update_df(self.df, COLUMNS_IN_SHOW, WIDTHS_IN_SHOW)
        self.destroy()