import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions.update import update_housing
from functions.search import id_exists
from functions.save_data import has_unsaved_changes
from config import WRITE_ALLOWED_FIELDS

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

class WindowUpdate(tk.Toplevel):
    def __init__(self, parent, df, update_func):
        super().__init__(parent)
        self.df = df
        self.update_func = update_func
        self.id = tk.StringVar()
        self.name = tk.StringVar()
        self.host_id = tk.StringVar()
        self.host_name = tk.StringVar()
        self.neighbourhood_group = tk.StringVar()
        self.neighbourhood = tk.StringVar()
        self.latitude = tk.StringVar()
        self.longitude = tk.StringVar()
        self.room_type = tk.StringVar()
        self.price = tk.StringVar()
        self.minimum_nights = tk.StringVar()
        self.availability = tk.StringVar()

        self.geometry('600x750')
        self.title('Update Housing')
        tk.Label(self, text='Update Housing', font=('Montserrat Medium', 16)).pack(
            side=tk.TOP, pady=16)

        # Canvas
        canvas = tk.Canvas(self)

        # Scrollbars
        h_scroll = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=h_scroll.set)

        # Frames
        main_frame = ttk.Frame(canvas)
        frame = ttk.Frame(main_frame)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)

        frame_top = ttk.Frame(main_frame)
        frame_top.columnconfigure(0, weight=1)
        frame_top.columnconfigure(1, weight=3)

        # Labels
        label_id = ttk.Label(frame_top, text='Housing ID')
        label_name = ttk.Label(frame, text='Housing Name')
        label_host_id = ttk.Label(frame, text='Host ID')
        label_host_name = ttk.Label(frame, text='Host Name')
        label_neighbourhood_group = ttk.Label(
            frame, text='Neighbourhood Group')
        label_neighbourhood = ttk.Label(frame, text='Neighbourhood')
        label_latitude = ttk.Label(frame, text='Latitude')
        label_longitude = ttk.Label(frame, text='Longitude')
        label_room_type = ttk.Label(frame, text='Room type')
        label_price = ttk.Label(frame, text='Price')
        label_minimum_nights = ttk.Label(frame, text='Minimum Nights')
        label_availability = ttk.Label(frame, text='Availability')

        # Input Fields
        entry_id = ttk.Entry(frame_top, textvariable=self.id, state=tk.ACTIVE)
        entry_name = ttk.Entry(frame, textvariable=self.name, state='readonly')
        entry_host_id = ttk.Entry(frame, textvariable=self.host_id, state='readonly')
        entry_host_name = ttk.Entry(frame, textvariable=self.host_name, state='readonly')
        entry_neighbourhood_group = ttk.Entry(
            frame, textvariable=self.neighbourhood_group, state='readonly')
        entry_neighbourhood = ttk.Entry(frame, textvariable=self.neighbourhood, state='readonly')
        entry_latitude = ttk.Entry(frame, textvariable=self.latitude, state='readonly')
        entry_longitude = ttk.Entry(frame, textvariable=self.longitude, state='readonly')
        entry_room_type = ttk.Entry(frame, textvariable=self.room_type, state='readonly')
        entry_price = ttk.Entry(frame, textvariable=self.price, state='readonly')
        entry_minimum_nights = ttk.Entry(
            frame, textvariable=self.minimum_nights, state='readonly')
        entry_availability = ttk.Entry(frame, textvariable=self.availability, state='readonly')

        self.entries = (self.name, self.host_id, self.host_name, self.neighbourhood_group, self.neighbourhood,
                        self.latitude, self.longitude, self.room_type, self.price, self.minimum_nights, self.availability)
        self.entry_widgets = (entry_name, entry_host_id, entry_host_name, entry_neighbourhood_group, entry_neighbourhood,
                        entry_latitude, entry_longitude, entry_room_type, entry_price, entry_minimum_nights, entry_availability)

        self.numeric_entries = (self.latitude, self.longitude, self.price,
                                self.host_id, self.availability, self.minimum_nights)

        # Placing Top
        label_id.grid(row=0, column=0, pady=16, padx=16, sticky='e')
        entry_id.grid(row=0, column=1, pady=16, padx=16, sticky='we')
        ttk.Button(frame_top, text='Find', command=self.find_housing).grid(row=1, columnspan=2, pady=16, padx=16, sticky='we')

        # Placing
        label_name.grid(row=0, column=0, pady=8, padx=16, sticky='e')
        label_host_id.grid(row=1, column=0, pady=8, padx=16, sticky='e')
        label_host_name.grid(row=2, column=0, pady=8, padx=16, sticky='e')
        label_neighbourhood_group.grid(row=3, column=0, pady=8, padx=16, sticky='e')
        label_neighbourhood.grid(row=4, column=0, pady=8, padx=16, sticky='e')
        label_latitude.grid(row=5, column=0, pady=8, padx=16, sticky='e')
        label_longitude.grid(row=6, column=0, pady=8, padx=16, sticky='e')
        label_room_type.grid(row=7, column=0, pady=8, padx=16, sticky='e')
        label_price.grid(row=8, column=0, pady=8, padx=16, sticky='e')
        label_minimum_nights.grid(row=9, column=0, pady=8, padx=16, sticky='e')
        label_availability.grid(row=10, column=0, pady=8, padx=16, sticky='e')

        entry_name.grid(row=0, column=1, pady=8, padx=16, sticky='we')
        entry_host_id.grid(row=1, column=1, pady=8, padx=16, sticky='we')
        entry_host_name.grid(row=2, column=1, pady=8, padx=16, sticky='we')
        entry_neighbourhood_group.grid(row=3, column=1, pady=8, padx=16, sticky='we')
        entry_neighbourhood.grid(row=4, column=1, pady=8, padx=16, sticky='we')
        entry_latitude.grid(row=5, column=1, pady=8, padx=16, sticky='we')
        entry_longitude.grid(row=6, column=1, pady=8, padx=16, sticky='we')
        entry_room_type.grid(row=7, column=1, pady=8, padx=16, sticky='we')
        entry_price.grid(row=8, column=1, pady=8, padx=16, sticky='we')
        entry_minimum_nights.grid(row=9, column=1, pady=8, padx=16, sticky='we')
        entry_availability.grid(row=10, column=1, pady=8, padx=16, sticky='we')

        frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        h_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Attaching Main Frame to Canvas
        canvas.create_window((0,0), window=main_frame, anchor="nw", tags='window')
        canvas.bind('<Configure>', lambda e: canvas.itemconfig('window', width=e.width))
        canvas.bind('<Configure>', lambda event, canvas=canvas: onFrameConfigure(canvas), add='+')

        # Action Buttons
        self.ok_button = ttk.Button(main_frame,
                   text='OK',
                   command=self.func_ok,
                   state=tk.DISABLED)
        self.ok_button.pack(side=tk.LEFT, expand=True, pady=32)

        ttk.Button(main_frame,
                   text='Cancel',
                   command=self.destroy).pack(side=tk.LEFT, expand=True, pady=32)

    def func_ok(self):
        if self.validate_inputs():
            for field, stringvar in zip(WRITE_ALLOWED_FIELDS, self.entries):
                update_housing(self.id.get(), field, stringvar.get())

            messagebox.showinfo(message=f'Housing {self.name.get()} Has Been Updated!')
            has_unsaved_changes(True)
            self.update_func(update_data=True)
            self.destroy()

    def validate_inputs(self):
        for entry in self.numeric_entries:
            if not entry.get():
                continue

            try:
                x = float(entry.get())
            except ValueError:
                messagebox.showerror(
                    message='Please Enter Valid Number for "Host ID", "Latitude", "Longitude", "Price", "Minimum Nights", and "Avaliability"')
                return False
        return True
    
    def find_housing(self):
        if not id_exists(self.id.get()):
            for widget in self.entry_widgets:
                if widget['state'] == 'readonly':
                    break
                widget.configure(state='readonly')

            messagebox.showerror(message='Housing Not Found')
            return
        else:
            housing = self.df[self.df['id'] == int(self.id.get())]
            housing = housing[WRITE_ALLOWED_FIELDS]
            for (i, entry), widget in zip(enumerate(self.entries), self.entry_widgets):
                value = housing[WRITE_ALLOWED_FIELDS[i]].to_string(index=False, header=False)
                entry.set(value)
                widget.configure(state='normal')
            self.ok_button['state']='normal'