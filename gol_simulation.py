import random
import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt


def init_universe(rows, cols):
    grid = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = round(random.random())
    return grid

def evolve(grid, pars):
    overcrowd, underpop, reproduction = pars
    rows, cols = grid.shape
    newgrid = np.zeros([rows, cols])
    neighbors = np.zeros([rows,cols])
    # Auxiliary padded grid
    padboard = np.zeros([rows+2, cols+2])
    padboard[:-2,:-2] = grid
    # Compute neighbours and newgrid
    for i in range(rows):
        for j in range(cols):
            neighbors[i][j] += sum([padboard[a][b] for a in [i-1, i, i+1] \
                                    for b in [j-1, j, j+1]])
            neighbors[i][j] -= padboard[i][j]
            # Evolution logic
            newgrid[i][j] = grid[i][j]
            if grid[i][j] and \
               (neighbors[i][j] > overcrowd or neighbors[i][j] < underpop):
                newgrid[i][j] = 0
            elif not grid[i][j] and neighbors[i][j] == reproduction:
                newgrid[i][j] = 1
    return newgrid
