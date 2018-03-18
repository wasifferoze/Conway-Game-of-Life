import matplotlib as mtl
mtl.use('Tkagg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np

import tkinter as tk
from tkinter import ttk


X = np.zeros((40, 40)) # 40 by 40 dead cells
# R-pentomino
X[23, 22:24] = 1
X[24, 21:23] = 1
X[25, 22] = 1

class Window():
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.f = Figure(figsize=(10, 9), dpi=80)
        self.fig = plt.figure(1)
        #self.fig.patch.set_facecolor('black')

        t = np.arange(0.0,0.3,0.01)
        s = np.sin(np.pi*t)
        plt.plot(t,s)
        # self.ax0 = self.f.add_axes((0.05, .05, .50, .50), facecolor=(.75, .75, .75), frameon=False)
        # self.ax1 = self.f.add_axes((0.05, .55, .90, .45), facecolor=(.75, .75, .75), frameon=False)
        # self.ax2 = self.f.add_axes((0.55, .05, .50, .50), facecolor=(.75, .75, .75), frameon=False)
        #
        # self.ax0.set_xlabel('Time (s)')
        # self.ax0.set_ylabel('Frequency (Hz)')
        # self.ax0.plot(np.max(np.random.rand(100, 10) * 10, axis=1), "r-")
        # self.ax1.plot(np.max(np.random.rand(100, 10) * 10, axis=1), "g-")
        # self.ax2.pie(np.random.randn(10) * 100)

        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.plot_widget = self.canvas.get_tk_widget()#.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.plot_widget.grid(row=0, column=0)
        #self.canvas.show()
        self.canvas.draw()

        # self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.frame)
        # self.toolbar.pack()
        # self.toolbar.update()


if __name__ == '__main__':
    root = tk.Tk()
    app = Window(master=root)
    root.title("MatplotLib with Tkinter")
    root.update()
    root.deiconify()
    root.mainloop()
