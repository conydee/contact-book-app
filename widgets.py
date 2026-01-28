import tkinter as tk
from tkinter.constants import HORIZONTAL


class Button(tk.Button):
    def __init__(self,parent, btntext):
        super().__init__(parent, bg="#3EB489",
                         font=("Comic Sans MS", 14),
                         text=btntext)

class Label(tk.Label):
    def __init__(self, parent, labeltext):
        super().__init__(parent, bg="lightgreen",
                         font=("Comic Sans MS", 14),
                         text=labeltext)

class Scale(tk.Scale):
    def __init__(self):
        super().__init__(orient=HORIZONTAL,
                         sliderlength=20,
                         from_= 0,
                         to= 10,
                         troughcolor="lightblue")

class Listbox(tk.Listbox):
    def __init__(self, parent):
        super().__init__(parent,
                         bg="#3EB489",
                         font=("Comic Sans MS", 14),
                         relief="solid",
                         borderwidth=2
                         )

class Entry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent,
                         bg="#3EB489",
                         font=("Comic Sans MS", 14),
                         relief="solid",
                         borderwidth=2
                         )

class Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,
                         bg="lightgreen"
                         )