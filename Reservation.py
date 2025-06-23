import tkinter as tk
from tkinter import ttk,messagebox
from database import create_connection
from EditReservation import EditReservationPage



class ReservationListPage(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack(pady=20)


        tk.Label(self,text="All reservations",font=("Arial",16,"bold")).pack(pady=10)
        tk.Button(self, text=" Back to Home", command=self.go_home).pack()
        tk.Button(self, text=" Edit Selected", command=self.edit_selected).pack(pady=5)



        self.tree=ttk.Treeview(self,columns=("ID","Name","Flight","Departure","Destination","Date","Seat"),show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col,text=col)
            self.tree.column(col,width=120,anchor="center")


        self.tree.pack(pady=10)

        tk.Button(self,text="Refresh",command=self.load_data).pack(pady=5)
        tk.Button(self,text="Delete Selected",command=self.delete_selected).pack(pady=5)
        self.load_data()

    def go_home(self):
        self.pack_forget()
        from home import HomePage
        HomePage(self.master)

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        db=create_connection()
        cr=db.cursor()
        cr.execute("SELECT * FROM flight ")
        rows=cr.fetchall()
        cr.close()

        for row in rows :
            self.tree.insert("","end",values=row)

    def delete_selected(self):
        selected_item=self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error","Please select a reservation to delete")
            return
        confirm=messagebox.askyesno("Confirm","Are you sure you want to delete this reservation ?")
        if not confirm:
            return

        try:
            item = self.tree.item(selected_item[0])
            reservation_id = item["values"][0]

            db = create_connection()
            cr = db.cursor()
            cr.execute("DELETE FROM flight WHERE id = ?", (reservation_id,))
            db.commit()
            db.close()

            messagebox.showinfo("Success", "Reservation deleted successfully!")
            self.load_data()

        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{e}")

    def edit_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a reservation to edit.")
            return

        item = self.tree.item(selected_item[0])
        reservation_data = item["values"]  # [id, name, flight, departure, destination, date, seat]

        self.pack_forget()
        EditReservationPage(self.master, reservation_data, self.back_after_edit)

    def back_after_edit(self):
        self.pack_forget()
        self.__init__(self.master)
