import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions.delete import delete_housing
from functions.save_data import has_unsaved_changes
from config import *

class WindowConfirm(tk.Toplevel):
    def __init__(self, parent, df, id, update_func):
        super().__init__(parent)
        self.df = df
        self.id = id
        self.update_func = update_func

        self.geometry('320x200')
        self.title('Confirm Deletion')
        tk.Label(self, text='Confirm Deletion', font=('Montserrat Medium', 16)).pack(side=tk.TOP, pady=16)
        
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        label = ttk.Label(frame, text='Are you sure want to delete this?')

        label.grid(row=0, column = 0, padx=10, pady= 10, sticky='se')

        frame.pack(fill=tk.BOTH, expand=True, anchor='center')

        ttk.Button(self,
                text='OK',
                command=self.func_ok).pack(side=tk.LEFT, expand=True, pady=32)

        ttk.Button(self,
                text='Cancel',
                command=self.destroy).pack(side=tk.LEFT, expand=True, pady=32)
        
    def func_ok(self):
        delete_housing(self.df, self.id)
        messagebox.showinfo(message=f'Housing {self.id} Has Been Deleted!')
        has_unsaved_changes(True)
        self.update_func(update_data=True)
        self.destroy()