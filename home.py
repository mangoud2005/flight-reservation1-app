import tkinter as tk
from tkinter import ttk
from booking import BookingPage
from Reservation import ReservationListPage




class HomePage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack(pady=50)

        tk.Label(self,text="Welcome to FlySky Reservations",font=("Arial",18,"bold")).pack(pady=10)
        tk.Label(self,text="Book your flights and manage your reservations",font=("Arial",12)).pack(pady=5)
        tk.Button(self, text="📝 Book a Flight", width=20, height=2, command=self.go_to_booking).pack(pady=15)
        tk.Button(self, text="📋 View Reservations", width=20, height=2, command=self.go_to_reservation).pack()

    def go_to_booking(self):
        self.pack_forget()
        BookingPage(self.master)

    def go_to_reservation(self):
        self.pack_forget()
        ReservationListPage(self.master)

    def go_home(self):
        self.pack_forget()
        HomePage(self.master)