import matplotlib as matplt
from matplotlib import animation
from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
from gol_simulation import init_universe, evolve

matplt.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

WIDTH = 803
HEIGHT = 506

pars = 3, 2, 3
rows, cols = 20, 20
fig = plt.figure()
ax = plt.axes()
im = ax.matshow(init_universe(rows, cols), cmap=plt.cm.binary)
ax.set_axis_off()


def init():
    im.set_data(init_universe(rows, cols))
    return (im,)

def animate(i):
    a = im.get_array()
    a = evolve(a, pars)
    im.set_array(a)
    return [im]


class GUI(tk.Frame):
    """for graphical interface

    -all user graphical interface are here
    """

    def __init__(self, master=None):
        super().__init__(master)
        # self.grid()
        # self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        # self.canvas.pack(side=tk.TOP)
        self.f1_style = ttk.Style()
        self.f1_style.configure('My.TFrame', background='#808080')
        self.control_area = ttk.Frame(self.master, style='My.TFrame', relief=RAISED, borderwidth=3)
        # self.control_area.config(background="#808080")
        self.control_area.grid(column=0, row=1)
        self.create_widgets()
        fig = plt.figure(1)
        # plt.ion()
        # t = np.arange(0.0, 3.0, 0.01)
        # s = np.sin(np.pi * t)
        # plt.plot(t, s)

        # anim.save('animation_random.mp4', fps=10)  # fps = FramesPerSecond
        canvas = FigureCanvasTkAgg(fig, master=win)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=0, column=0)
        anim = animation.FuncAnimation(canvas, animate, init_func=init, frames=100, interval=300, blit=True)
    def create_widgets(self):
        """all widget code is here"""

        # tk.Button(win, text="Update", command=self.update).grid(row=1, column=1)
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

        self.stop = tk.Button(self.control_area, text="Fast", fg="red", command=self.stop_game)
        self.stop.pack(side=tk.LEFT, padx=3, pady=2)
        self.gen_label = tk.Label(win, text="label", bg="#808080")
        self.gen_label.grid(row=0, column=1)

    def combo_callback(self, eventobj):
        """this method get combobox events"""
        print(self.combo_input.get())  # print name
        print(self.combo_input.current())  # print index

    def start_game(self):
        """game start flag on and off code here"""
        print("hi there, game started!")
        self.draw()

    def stop_game(self):
        print("hi there! game stopped")

    def next_generation(self):
        print("next generation")

    def draw(self):
        for i in range(10):
            for j in range(10):
                # if self.u.space[i][j] == 1:
                self.canvas.create_rectangle(
                    j, i, j, i, fill="black")

    def update(self):
        s = np.cos(np.pi * t)
        plt.plot(self.t, s)
        # d[0].set_ydata(s)
        self.fig.canvas.draw()


win = tk.Tk()
win.title("Conway's Game of Life")
win.resizable(0, 0)
win.geometry("803x506")
app_gui = GUI(master=win)
win.mainloop()
np.random.seed(0)
X = np.zeros((30, 40), dtype=bool)
r = np.random.random((10, 20))
X[10:20, 10:30] = (r > 0.75)
