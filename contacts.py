import tkinter as tk
from widgets import Label, Button, Scale, Entry

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x800")
        self.title("Contact Book")

        #my frame is green
        self.label1 = Label(self, "ion like poopies")
        self.label1.pack(pady=20)

        self.entry1 = Entry(self)
        self.entry1.pack()

root = MainApp()
root.mainloop()
