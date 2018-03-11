from tkinter import *
import tkinter as tk
from  tkinter import ttk

class GUI(tk.Frame):
    """for graphical interface"""
    WIDTH = 803
    HEIGHT = 506

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side=tk.TOP)
        self.control_area = tk.Frame(self)
        self.control_area.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self.control_area, text="Start", command=self.start_game)
        self.start.pack(side=tk.RIGHT)
        self.stop = tk.Button(self.control_area, text="Stop", fg="red", command=self.stop_game)
        self.stop.pack(side=tk.RIGHT)
        tkvar = tk.StringVar(win)
        # Dictionary with options
        choices = ('Clear', 'Small Glider', 'Glider', 'Exploder', '10 Cell Row', 'Light Weight Spaceship', 'Tumbler',
                   'Gosper Glider Gu')
        tkvar.set('Clear')  # set the default option
        popupMenu = tk.OptionMenu(self.control_area, tkvar, *choices)
        popupMenu.pack(side=tk.LEFT)
        ttk.Combobox(self.control_area, values=choices).pack(side=tk.LEFT)
    def start_game(self):
        print("hi there, game started!")

    def stop_game(self):
        print("hi there! game stopped")


win = tk.Tk()
#win.geometry('+%d+%d' % (200, 200))
app_gui = GUI(master=win)
win.mainloop()
