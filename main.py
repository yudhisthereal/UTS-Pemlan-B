from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions.show import *
from functions.search import *
from functions.delete import *
from functions.add import *
from functions.update import *
from config import get_temp_path
from functions.save_data import *
import csv
import pandas as pd

if get_temp_path() == None:
    create_temp()

df = pd.read_csv(get_temp_path())


def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))


class Table():

    def __init__(self, root, data, headers):
        canvas = Canvas(root)
        frame = ttk.Frame(canvas)
        frame_head = ttk.Frame(root)

        scroll = ttk.Scrollbar(root, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scroll.set)

        frame_head.pack(side=TOP, fill=X)
        scroll.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        canvas.create_window((4, 4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event,
                   canvas=canvas: onFrameConfigure(canvas))

        total_rows = len(data.index)
        if total_rows > 50:
            total_rows = 50
        # code for creating table
        width = (5, 50, 15, 25, 5)
        for i, header in enumerate(headers):
            self.e = ttk.Entry(
                frame_head, width=width[i], font=('Montserrat Medium', 11))

            self.e.grid(row=0, column=i, sticky='n')
            self.e.insert(END, header.title())

        for i in range(1, total_rows):
            for j, header in enumerate(headers):
                self.e = ttk.Entry(frame, width=width[j],
                                   font=('Montserrat', 11))

                self.e.grid(row=i+1, column=j)
                self.e.insert(END, data.iloc[i][header])


def darkstyle(root):
    root.tk.call('source', 'theme/azure.tcl')
    root.tk.call('set_theme', 'dark')


def main_window():
    window = Tk()
    window.geometry('1080x720+100+32')
    window.title("NYC Housing Admin")
    window.resizable(False, False)
    darkstyle(window)

    title_font = ('Montserrat Bold', 24)
    title = ttk.Label(window, text='NYC Housing Admin', font=title_font)
    title.pack(side=TOP, pady=16)

    return window


def create_menu(root):
    frame = ttk.Frame(root)
    frame.pack(side=TOP, pady=32)

    # menu_width = 10
    help_button = ttk.Button(
        master=frame, command=func_help, text="Help")
    show_button = ttk.Button(
        master=frame, command=func_show, text="Show Data")
    search_button = ttk.Button(
        master=frame, command=func_search, text="Search")
    add_button = ttk.Button(master=frame, command=func_add,
                            text="Add")
    update_button = ttk.Button(
        master=frame, command=func_update, text="Update")
    delete_button = ttk.Button(
        master=frame, command=func_delete, text="Delete")
    save_button = ttk.Button(
        master=frame, command=func_save, text="Save Changes")
    exit_button = ttk.Button(
        master=frame, command=func_exit, text="Exit")

    for i, widget in enumerate(frame.winfo_children()):
        widget.grid(row=0, column=i, padx=8, pady=5, sticky='nesw')


def create_table(root):
    table = Table(root, df, COLUMNS_IN_SHOW)
    return table


def func_help():
    pass


def func_show():
    pass


def func_search():
    pass


def func_add():
    pass


def func_update():
    pass


def func_delete():
    pass


def func_save():
    pass


def func_exit():
    if has_unsaved_changes() == True:
        should_save = messagebox.askyesnocancel(title='Warning', message='Save Changes?')
        if should_save == None:
            return
        elif should_save:
            save()
    destroy_temp()
    window.destroy()
    quit()


# Main Window
window = main_window()
window.protocol('WM_DELETE_WINDOW', func_exit)

# Content
create_menu(window)
table = create_table(window)

if __name__ == '__main__':
    window.mainloop()
