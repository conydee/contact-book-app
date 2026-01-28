import tkinter as tk
from widgets import Label, Button, Scale, Entry, Frame, Listbox

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #configurations
        self.geometry("700x800")
        self.title("Contact Book")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        #frames

        self.frame1 = Frame(self)
        self.frame1.configure(relief="solid", borderwidth=3)
        self.frame1.grid( column=1, row = 0, rowspan=3, sticky="news", pady=40, padx=20)

        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=5)
        self.frame1.rowconfigure(2, weight=5)
        self.frame1.rowconfigure(3, weight=5)
        self.frame1.rowconfigure(4, weight=5)
        self.frame1.columnconfigure(0, weight=1)

        self.frame2 = Frame(self)
        self.frame2.configure(relief="solid", borderwidth=3)
        self.frame2.grid( column=0, row = 0, rowspan=3, sticky="news", pady=40, padx=20)

        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.rowconfigure(2, weight=1)
        self.frame2.columnconfigure(0, weight=1)


        #widgets

        self.entry1 = Entry(self.frame2)
        self.entry1.grid(row=0, column=0)

        self.listbox1 = Listbox(self.frame2)
        self.listbox1.grid(row=1, column=0, sticky="news", padx=20)

        self.label1 = Label(self.frame1, "Contact Book")
        self.label1.grid(row=0, column=0, sticky="news")

        self.button1 = Button(self.frame1, "Add contact")
        self.button1.grid(row=1, column=0, sticky="news", padx=20, pady=20)

        self.button2 = Button(self.frame1, "Delete contact")
        self.button2.grid(row=2, column=0, sticky="news", padx=20, pady=20)

        self.button3 = Button(self.frame1, "Save contacts")
        self.button3.grid(row=3, column=0, sticky="news", padx=20, pady=20)

        self.button4 = Button(self.frame1, "Load contacts")
        self.button4.grid(row=4, column=0, sticky="news", padx=20, pady=20)





root = MainApp()
root.mainloop()
