import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from menu_windows.window_confirm import WindowConfirm
from functions.search import id_exists

class WindowDelete(tk.Toplevel):
    def __init__(self, parent, df, update_func):
        super().__init__(parent)
        self.parent = parent
        self.df = df
        self.update_func = update_func
        self.id = tk.StringVar()

        self.geometry('320x200')
        self.title('Delete Housing')
        tk.Label(self, text='Delete Housing', font=('Montserrat Medium', 16)).pack(side=tk.TOP, pady=16)
        
        # Entries
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        label_id = ttk.Label(frame, text='ID')
        # label_searchby = ttk.Label(frame, text='Search by')

        entry_id = ttk.Entry(frame, textvariable=self.id)

        label_id.grid(row=0, column = 0, padx=10, pady= 10, sticky='se')
        # label_searchby.grid(row=1, column = 0, padx=10, pady=10, sticky='ne')

        entry_id.grid(row=0, column=1, padx=10, pady=10, sticky='sw')

        frame.pack(fill=tk.BOTH, expand=True, anchor='center')

        ttk.Button(self,
                text='OK',
                command=self.find_housing).pack(side=tk.LEFT, expand=True, pady=12)

        ttk.Button(self,
                text='Cancel',
                command=self.destroy).pack(side=tk.LEFT, expand=True, pady=12)

    def func_confirm(self):
        WindowConfirm(self.parent, self.df, self.id.get(), self.update_func).grab_set()
        
    def find_housing(self):
        if not id_exists(self.id.get()):
            messagebox.showerror(message='Housing Not Found')
            return
        else:
            self.func_confirm()
            self.destroy()