import tkinter as tk
from tkinter import messagebox
from database import create_connection



class BookingPage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack(pady=20)

        tk.Label(self,text=" Book a Fligh",font=("Arail",16,"bold")).pack(pady=10)
        self.name_var=tk.StringVar()
        self.flight_var=tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_var = tk.StringVar()

        self.build_form()

        tk.Button(self, text="️ Back to Home", command=self.go_home).pack()

    def go_home(self):
        self.pack_forget()
        from home import HomePage
        HomePage(self.master)

    def build_form(self):
        fields=[
            ("Passegner Name:",self.name_var),
            ("Flight Number:",self.flight_var),
            ("Departure :",self.departure_var),
            ("Destination :",self.destination_var),
            ("Date (YYYY-MM-DD):",self.date_var),
            ("Seat Number: ",self.seat_var)

        ]

        for label_text, var in fields:
            frame=tk.Frame(self)
            tk.Label(frame, text=label_text,width=20 ,anchor="w").pack(side="left")
            tk.Entry(frame,textvariable=var,width=30).pack(side="left")
            frame.pack(pady=5)

        tk.Button(self,text="Submit Booking",command=self.submit_booking).pack(pady=15)


    def submit_booking(self):
        name=self.name_var.get()
        flight=self.flight_var.get()
        departure=self.departure_var.get()
        destination=self.destination_var.get()
        date=self.date_var.get()
        seat=self.seat_var.get()

        if not all([name,flight,departure,destination,date,seat]):
            messagebox.showerror("Error","plz fill up all fields ")
            return

        db = create_connection()
        cr = db.cursor()
        cr.execute("""
            INSERT INTO flight (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, flight, departure, destination, date, seat))
        db.commit()
        db.close()

        messagebox.showinfo("Success","Flight booked successfully! ")

        self.name_var.set("")
        self.flight_var.set("")
        self.departure_var.set("")
        self.destination_var.set("")
        self.date_var.set("")
        self.seat_var.set("")

        self.pack_forget()
        from Reservation import ReservationListPage
        ReservationListPage(self.master)



