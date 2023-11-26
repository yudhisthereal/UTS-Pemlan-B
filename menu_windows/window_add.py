import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions.add import add_housing
from functions.save_data import has_unsaved_changes


class WindowAdd(tk.Toplevel):
    def __init__(self, parent, df, update_data):
        super().__init__(parent)
        self.df = df
        self.update_data = update_data
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

        self.geometry('600x720')
        self.title('Add Housing')
        tk.Label(self, text='Add Housing', font=('Montserrat Medium', 16)).pack(
            side=tk.TOP, pady=16)
        

        # Frame
        frame = ttk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=3)

        # Labels
        label_name = ttk.Label(frame, text='Housing Name')
        label_host_id = ttk.Label(frame, text='Host ID')
        label_host_name = ttk.Label(frame, text='Host Name')
        label_neighbourhood_group = ttk.Label(frame, text='Neighbourhood Group')
        label_neighbourhood = ttk.Label(frame, text='Neighbourhood')
        label_latitude = ttk.Label(frame, text='Latitude')
        label_longitude = ttk.Label(frame, text='Longitude')
        label_room_type = ttk.Label(frame, text='Room type')
        label_price = ttk.Label(frame, text='Price')
        label_minimum_nights = ttk.Label(frame, text='Minimum Nights')
        label_availability = ttk.Label(frame, text='Availability')

        # Input Fields
        entry_name = ttk.Entry(frame, textvariable=self.name)
        entry_host_id = ttk.Entry(frame, textvariable=self.host_id)
        entry_host_name = ttk.Entry(frame, textvariable=self.host_name)
        entry_neighbourhood_group = ttk.Entry(frame, textvariable=self.neighbourhood_group)
        entry_neighbourhood = ttk.Entry(frame, textvariable=self.neighbourhood)
        entry_latitude = ttk.Entry(frame, textvariable=self.latitude)
        entry_longitude = ttk.Entry(frame, textvariable=self.longitude)
        entry_room_type = ttk.Entry(frame, textvariable=self.room_type)
        entry_price = ttk.Entry(frame, textvariable=self.price)
        entry_minimum_nights = ttk.Entry(frame, textvariable=self.minimum_nights)
        entry_availability = ttk.Entry(frame, textvariable=self.availability)

        self.numeric_entries = (self.latitude, self.longitude, self.price, self.host_id, self.availability, self.minimum_nights)

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

        frame.pack(fill=tk.BOTH, expand=True, anchor='center')

        # Action Buttons
        ttk.Button(self,
                   text='OK',
                   command=self.func_ok).pack(side=tk.LEFT, expand=True, pady=32)

        ttk.Button(self,
                   text='Cancel',
                   command=self.destroy).pack(side=tk.LEFT, expand=True, pady=32)

    def func_ok(self):
        if self.validate_inputs():
            add_housing(self.df, self.name.get(), self.host_id.get(), self.host_name.get(), 
                    self.neighbourhood_group.get(), self.neighbourhood.get(), self.latitude.get(), 
                    self.longitude.get(), self.room_type.get(), self.price.get(), 
                    self.minimum_nights.get(), self.availability.get()
                )
            messagebox.showinfo(message=f'Housing {self.name.get()} Has Been Added!')
            has_unsaved_changes(True)
            self.update_data(update_data=True)
            self.destroy()
        
    
    def validate_inputs(self):
        for entry in self.numeric_entries:
            try:
                x = float(entry.get())
            except ValueError:
                messagebox.showerror(message='Please Enter Valid Number for "Host ID", "Latitude", "Longitude", "Price", "Minimum Nights", and "Avaliability"')
                return False
        return True
