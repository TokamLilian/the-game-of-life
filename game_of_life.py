from random import *
import turtle
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


def position(x, y):
#this function places the turtle at a certain point
    
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def draw_alive(square_size):
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(4):
        fd(square_size); lt(90)
    
    turtle.end_fill()
    turtle.color("black")


def draw_death(square_size):
    for _ in range(4):
        fd(square_size); lt(90)


def draw(grid):

    size = len(grid)
    square_size = 40
    for i in range (size):

        for j in range (size):

            row = j // size
            col = j % size

            cell_state = grid[row][col]
            index = row*size + col

            position(i*square_size, j*square_size)
            if cell_state == 1: draw_alive(index)
            else: draw_death(index)


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
            neighbours.append(grid[i//size][i%size])

    return neighbours


def decide_next(grid, cell_index, cell_status):
#this function determines if a 0 cell has 3 live neighbours inorder to make it alive
#this function determines if a cell 1 has less than 2 live cells or greater than three live cells to make it die

    size = len(grid)
    new_grid = grid

    alive_neighbours = 0
    neighbours = get_neighbour(grid, cell_index)

    for value in neighbours:
    #we determine the amount of alive neighbours of the 0
        if value == 1:
            alive_neighbours += 1

    if cell_status == 0:
        if alive_neighbours == 3:
            new_grid[cell_index//size][cell_index%size] = 1 

    elif cell_status == 1:
        if alive_neighbours < 2 or alive_neighbours > 3:
            new_grid[cell_index//size][cell_index%size] = 0

    return new_grid


def decide(old_grid):
#this function goes through the grid and inspects if a cell will be set alive or death

    #old_grid = grid
    size = len(old_grid)
    
    for i in range (size):

        for j in range (size):
            row = j // size
            col = j % size

            cell_state = old_grid[row][col]
            
            new_grid = decide_next(old_grid, (row*size) + col, cell_state)

    draw(new_grid)

    return new_grid


def init():

    turtle.delay(20)
    grid = create_array(3)

    while True:
        grid = decide(grid)

    #turtle.exitonclick()

#init()