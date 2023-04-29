from random import *
from turtle import *

def create_array(size):
#this function returns a sizexsize matrix as a two-dimensional array 

    if size < 0: return None

    grid = [None] * size

    for i in range (size):
        grid[i] = [None] * size

    for j in range ( size**2 ):
        row = j // size
        col = j % size
        value = randint(0, 1)
        grid[row][col] = value

    return grid

def draw_alive():
    pass


def draw_death():
    pass


def get_neighbour(grid, index):
#this function returns the eight neighbours of a cell
    size = len(grid)

    left = -1 if index % size == 0 else index - 1
    right = -1 if (index + 1) % size == 0 else index + 1
    up = -1 if index < size else index - size
    down = -1 if index > size*(size - 1) else index + size

    diag_lu = -1 if left == -1 or up == -1 else index - size - 1
    diag_ru = -1 if right == -1 or up == -1 else index - size + 1
    diag_rd = -1 if right == -1 or down == -1 else index + size + 1
    diag_ld = -1 if left == -1 or down == -1 else index + size - 1

    neighbours = []
    index_max = size ** 2 - 1
    for i in [left, right, up, down, diag_lu, diag_ru, diag_rd, diag_ld]:
        if i >= 0 and i <= index_max:
            neighbours.append(i)

    return neighbours


def decide_zero(grid, cell_index):
#this function determines if a 0 cell has 3 live neighbours inorder to make it alive

    neighbours = get_neighbour(grid, cell_index)
    pass


def decide_one(grid, cell_index):
#this function determines if a cell 1 has less than 2 live cells or greater than three live cells to make it die

    neighbours = get_neighbour(grid, cell_index)
    pass


def decide(grid):
#this function goes through the grid and inspects if a cell will be set alive or death

    size = len(grid)
    for i in range (size):

        for j in range (size):
            row = j // size
            col = j % size

            cell_state = grid[row][col]
            
            if cell_state == 1: decide_one(grid, (row*size) + col)
            else: decide_zero(grid, (row*size) + col)


def init():

    print(create_array(6))

init()

