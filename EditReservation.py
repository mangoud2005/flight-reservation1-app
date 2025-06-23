import tkinter as tk
from dataclasses import fields
from tkinter import ttk, messagebox
from database import create_connection



class EditReservationPage(tk.Frame):
    def __init__(self,master,reservation_data,go_back_callback):
        super().__init__(master)
        self.master=master
        self.reservation_id=reservation_data[0]
        self.go_back_callback=go_back_callback
        self.pack(pady=20)

        tk.Label(self,text="Edite",font=("Arial",16,"bold")).pack(pady=10)

        self.name_var=tk.StringVar(value=reservation_data[1])
        self.flight_var=tk.StringVar(value=reservation_data[2])
        self.departure_var = tk.StringVar(value=reservation_data[3])
        self.destination_var = tk.StringVar(value=reservation_data[4])
        self.date_var = tk.StringVar(value=reservation_data[5])
        self.seat_var = tk.StringVar(value=reservation_data[6])
        tk.Button(self, text=" Back to Home", command=self.go_home).pack()
        self.build_form()


    def go_home(self):
        self.pack_forget()
        from home import HomePage
        HomePage(self.master)

    def build_form(self):
        feilds=[
            ("Passenger Name :",self.name_var),
            ("Flight Number :",self.flight_var),
            ("Departure :",self.departure_var),
            ("Destination :",self.destination_var),
            ("Date (YYYY-MM-DD):",self.date_var),
            ("Seat Number :",self.seat_var)

        ]

        for label_text,var in feilds:
            frame=tk.Frame(self)
            tk.Label(frame, text=label_text, width=18, anchor="w").pack(side="left")
            tk.Entry(frame, textvariable=var, width=30).pack(side="left")
            frame.pack(pady=5)

        tk.Button(self, text=" Update Reservation", command=self.update_reservation).pack(pady=10)


    def update_reservation(self):
        name = self.name_var.get()
        flight = self.flight_var.get()
        departure = self.departure_var.get()
        destination = self.destination_var.get()
        date = self.date_var.get()
        seat = self.seat_var.get()

        if not all([name, flight, departure, destination, date, seat]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            db = create_connection()
            cr = db.cursor()
            cr.execute("""
                UPDATE flight
                SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            """, (name, flight, departure, destination, date, seat, self.reservation_id))
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.go_back_callback()

        except Exception as e:
            messagebox.showerror("Database Error", f"Database is locked or busy:\n{e}")

