import sys
from random import *
import turtle
from turtle import *
from copy import *

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


def draw_box(size, square_size):
    
    position(0, square_size)
    rt(90)
    for _ in range(4):
        fd(size); lt(90)
    lt(90)
    #goto(-turtle.window_width()/2, (turtle.window_height()/2)-square_size)
    position(0, -square_size)


def draw_alive(square_size):
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(4):
        fd(square_size); lt(90)
    
    turtle.end_fill()
    turtle.color("black")


def draw(grid, square_size):
    pu();goto(-turtle.window_width()/2, turtle.window_height()/2);pd()

    size = len(grid)
    width = size*square_size
    pu();draw_box(width, square_size);pd() ##

    for i in range (size):

        for j in range (size):

            row = j // size
            col = j % size

            cell_state = grid[i+row][col]

            if cell_state == 1: 
                position(j*square_size, -i*square_size)
                draw_alive(square_size)
                position(-j*square_size, i*square_size)


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


def decide_next(neighbours, cell_index, cell_status, grid):
#this function determines if a 0 cell has 3 live neighbours inorder to make it alive
#this function determines if a cell 1 has less than 2 live cells or greater than three live cells to make it die

    size = len(grid)

    alive_neighbours = 0

    for value in neighbours:
    #we determine the amount of alive neighbours of the 0
        if value == 1:
            alive_neighbours += 1

    if cell_status == 0:
        if alive_neighbours == 3:
            grid[cell_index//size][cell_index%size] = 1 

    elif cell_status == 1:
        if alive_neighbours < 2 or alive_neighbours > 3:
            grid[cell_index//size][cell_index%size] = 0

    return grid


def decide(grid, square_size):
#this function goes through the grid and inspects if a cell will be set alive or death

    """ We need to store the value of the grid in such a way that it is not
        modified by new_grid coming from decicde_next function but edits 
        are done on the new grid from time to time"""
    size = len(grid)

    old_grid = deepcopy(grid)
    
    for i in range (size):

        for j in range (size):
            row = j // size
            col = j % size

            cell_index= ((i+row)*size) + col
            cell_state = grid[i+row][col]

            neighbours = get_neighbour(old_grid, cell_index)
            new_grid = decide_next(neighbours, cell_index, cell_state, grid)

    draw(new_grid, square_size)

    return new_grid

def update_grid(i, j):
#to update the grid and proceed to next verification
    print('x', i, 'and y', j) ##
    grid = []
    return grid


def init():

    def get_inputs():
        try:
            array_size = int(input('Select dimension: '))
            square_size = int(input('Enter square size: '))
            return [array_size, square_size]
        except:
            get_inputs() 

    if len(sys.argv) == 3:
        try:
            array_size = int(sys.argv[1])                            #ces arguments vont etre utilisés pour se connecter à l'API
            square_size = int(sys.argv[2])                            

        except:
            information = get_inputs()
            array_size = information[0]
            square_size = information[1]

    else: 
          information = get_inputs()
          array_size = information[0]
          square_size = information[1]

    screen = turtle.Screen()
    screen.setup(width = 0.9, height = 0.9)
    canvas = screen.getcanvas() 
    root = canvas.winfo_toplevel()
    root.overrideredirect(0)

    turtle.delay(0)
    turtle.hideturtle()
    grid = create_array(array_size)
    
    while True:
        grid = decide(grid, square_size)
        turtle.onscreenclick(update_grid, 1)
        turtle.listen()
        turtle.clear()

init()

def take_click():
    draw_box(100)
    turtle.onscreenclick(update_grid, 1)
    turtle.listen()
    turtle.done()