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
#this function places the turtle at a relative point
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def setup_screen(size, square_size, gap):
    width = size*square_size

    screen = turtle.Screen()
    screen.setup(width = 0.9, height = 0.9)
    canvas = screen.getcanvas() 
    root = canvas.winfo_toplevel()
    root.overrideredirect(0)

    turtle.delay(0)
    turtle.hideturtle()

    pu(); goto(-turtle.window_width()/2, turtle.window_height()/2); pd()
    #pu();draw_box(width, square_size, gap);pd() ##


def draw_box(width, square_size, gap):
#this function draws a box in which the game takes place        
    position(0, square_size)
    rt(90)
    for _ in range(4):
        #fd(width); lt(90)
        fd(width + gap); lt(90)
    lt(90)
    #position(0, -square_size)
    position(gap/2, -square_size-(gap/2))


def draw_cell(square_size, colour):
#this function draws an alive cell
    turtle.color(colour)
    turtle.begin_fill()
    for _ in range(4):
        fd(square_size); lt(90)
    
    turtle.end_fill()
    turtle.color("black")


def draw(grid, square_size, size, gap):
#this function goes through the two-dimensional array representing the grid inorder to proceed with drawing of alive cells or not

    for i in range (size):

        for j in range (size):

            row = j // size
            col = j % size

            cell_state = grid[i+row][col]

            position(j*square_size, -i*square_size)
            if cell_state == 1: 
                draw_cell(square_size, "blue")
            else: draw_cell(square_size, "white")
            position(-j*square_size, i*square_size)

    #position(-gap/2, gap/2)                         #to place the turtle at the original position on the grid for the next executiion


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


def decide_next(neighbours, cell_index, cell_status, grid, size):
#this function determines if a 0 cell has 3 live neighbours inorder to make it alive
#this function determines if a cell 1 has less than 2 live cells or greater than three live cells to make it die

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


def decide(grid, square_size, size, gap):
#this function goes through the grid and inspects if a cell will be set alive or death

    """ We need to store the value of the grid in such a way that it is not
        modified by new_grid coming from decicde_next function but edits 
        are done on the new grid from time to time"""

    old_grid = deepcopy(grid)
    
    for i in range (size):

        for j in range (size):
            row = j // size
            col = j % size

            cell_index= ((i+row)*size) + col
            cell_state = grid[i+row][col]

            neighbours = get_neighbour(old_grid, cell_index)
            new_grid = decide_next(neighbours, cell_index, cell_state, grid, size)

    draw(new_grid, square_size, size, gap)

    return new_grid


def update_grid(x, y, grid, size, square_size):
#to update the grid and proceed to next verification

    # -576 <= x <= (size*sqaure_size) - 576
    # 380 - (size*square_size) <= y <= 285
    lx = -576                           #the lower boundary of x on the canvas
    uy = 285                            #the upper boundary of y on the canvas

    x = abs(lx - x)
    y = abs(y - uy)

    x_pos = int(x//square_size)         #to know position of the cell
    y_pos = int(y//square_size)

    i = size - 1 - y_pos                #to get the index of the cell's value in the grid
    j = x_pos

    #print('x position', x_pos, 'and y position', y_pos)
    #square = grid[i][j]
    #print('The square is', square)

    grid[i][j] = 1                      #change the clicked cell to alive
    

def init():
#this function begins the program execution

    def get_inputs():
        try:
            array_size = int(input('Select dimension: '))
            square_size = int(input('Enter square size: '))
            return [array_size, square_size]
        except:
            get_inputs() 

    if len(sys.argv) == 3:
        try:
            array_size = int(sys.argv[1])
            square_size = int(sys.argv[2])                            

        except:
            information = get_inputs()
            array_size = information[0]
            square_size = information[1]

    else: 
          information = get_inputs()
          array_size = information[0]
          square_size = information[1]

    grid = create_array(array_size)
    
    size = len(grid)
    #gap = square_size/size 
    #if gap < 1: gap **= -1      #to take the dividend of both values
    #elif gap == 1: gap = 5      #take an arbitray value
    gap = 10
    
    setup_screen(size, square_size, gap)

    while True:
        grid = decide(grid, square_size, size, gap)
        turtle.onscreenclick(lambda x, y: update_grid(x, y, grid, size, square_size))
        turtle.listen()
        #turtle.clear()

init()