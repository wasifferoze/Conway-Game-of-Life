from tkinter import *
import tkinter as tk
from  tkinter import ttk


class GUI(tk.Frame):
    """for graphical interface

    -all user graphical interface are here
    """
    WIDTH = 803
    HEIGHT = 506

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side=tk.TOP)
        self.control_area = tk.Frame(self, relief=RAISED, borderwidth=3)
        self.control_area.config(bg="#808080")
        self.control_area.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        self.create_widgets()

    def create_widgets(self):
        """all widget code is here"""
        tkvar = tk.StringVar(win)
        # Dictionary with options
        choices = ('Clear', 'Small Glider', 'Glider', 'Exploder', '10 Cell Row', 'Light Weight Spaceship', 'Tumbler',
                   'Gosper Glider Gu')
        self.combo_input = ttk.Combobox(self.control_area, width=25, values=choices, state='readonly')
        self.combo_input.pack(side=tk.LEFT)
        self.combo_input.current(0)
        self.combo_input.bind("<<ComboboxSelected>>", self.combo_callback)

        self.next = tk.Button(self.control_area, text="Next", command=self.next_generation)
        self.next.pack(side=tk.LEFT, padx=3, pady=2)
        self.start = tk.Button(self.control_area, text="Start", command=self.start_game)
        self.start.pack(side=tk.LEFT, padx=3, pady=2)

        self.stop = tk.Button(self.control_area, text="Stop", fg="red", command=self.stop_game)
        self.stop.pack(side=tk.LEFT, padx=3, pady=2)

        self.gen_label = tk.Label(self.control_area, text="label", bg="#808080")
        self.gen_label.pack(side=tk.RIGHT)


    def combo_callback(self, eventobj):
        """this method get combobox events"""
        print(self.combo_input.get())   # print name
        print(self.combo_input.current())   # print index

    def start_game(self):
        """game start flag on and off code here"""
        print("hi there, game started!")

    def stop_game(self):
        print("hi there! game stopped")

    def next_generation(self):
        print("next generation")


win = tk.Tk()
win.title("Conway's Game of Life")
win.resizable(0,0)
# win.geometry('+%d+%d' % (200, 200))
app_gui = GUI(master=win)
win.mainloop()
