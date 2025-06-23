import tkinter as tk
from home import HomePage


if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("500x500")
    root.title("Flight Reservation App")
    HomePage(root)
    root.mainloop()

