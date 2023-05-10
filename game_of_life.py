import sys
from random import *
import turtle
from turtle import *
from copy import *

def create_array(lines, columns):
#this function returns a sizexsize matrix as a two-dimensional array 

    if columns <= 0 or lines <= 0: return None

    grid = [None] * lines

    for i in range (lines):
        grid[i] = [None] * columns

    for j in range ( columns * lines ):
        row = j // columns
        col = j % columns
        value = randint(0, 1)
        grid[row][col] = value

    return grid


def position(x, y):
#this function places the turtle at a relative point
    pu(); fd(x); lt(90); fd(y); rt(90); pd()


def setup_screen():
    screen = turtle.Screen()
    screen.setup(width = 0.9, height = 0.9)
    canvas = screen.getcanvas() 
    root = canvas.winfo_toplevel()
    root.overrideredirect(0)
    screen.bgcolor("black")

    turtle.delay(0)
    turtle.hideturtle()

    lx = -turtle.window_width()/2                          #the lower boundary of x on the canvas
    uy = turtle.window_height()/2                          #the upper boundary of y on the canvas
    
    pu(); goto(lx, uy); pd()
    return [lx , uy]


def draw_cell(square_size, colour):
#this function draws an alive cell
    turtle.color(colour)
    turtle.begin_fill()
    for _ in range(4):
        fd(square_size); lt(90)
    
    turtle.end_fill()


def draw(grid, square_size, lines, columns, gap):
#this function goes through the two-dimensional array representing the grid inorder to proceed with drawing of alive cells or not

    for i in range (lines):

        for j in range (columns):

            row = j // columns
            col = j % columns

            cell_state = grid[i+row][col]

            position(j*square_size, -i*square_size)
            if cell_state == 1: 
                draw_cell(square_size, "green")
            else: draw_cell(square_size, "black")
            position(-j*square_size, i*square_size)


def get_neighbour(grid, index, lines, columns):
#this function returns the eight neighbours of a cell

    left = -1 if index % columns == 0 else index - 1
    right = -1 if (index + 1) % columns == 0 else index + 1
    up = -1 if index < columns else index - columns
    down = -1 if index > columns*(columns - 1) else index + columns

    diag_lu = -1 if left == -1 or up == -1 else index - columns - 1
    diag_ru = -1 if right == -1 or up == -1 else index - columns + 1
    diag_rd = -1 if right == -1 or down == -1 else index + columns + 1
    diag_ld = -1 if left == -1 or down == -1 else index + columns - 1

    neighbours = []
    index_max = (lines * columns) - 1
    for i in [left, right, up, down, diag_lu, diag_ru, diag_rd, diag_ld]:
        if i >= 0 and i <= index_max:
            neighbours.append(grid[i//columns][i%columns])

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


def decide(grid, lines, columns):
#this function goes through the grid and inspects if a cell will be set alive or death

    """ We need to store the value of the grid in such a way that it is not
        modified by new_grid coming from decicde_next function but edits 
        are done on the new grid from time to time"""

    old_grid = deepcopy(grid)
    
    for i in range (lines):

        for j in range (columns):
            col = j % columns

            cell_index= (i*columns) + col
            cell_state = grid[i][col]

            neighbours = get_neighbour(old_grid, cell_index, lines, columns)
            new_grid = decide_next(neighbours, cell_index, cell_state, grid, columns)

    return new_grid


def update_grid(x, y, grid, lines, columns, square_size, lx, uy):
#to update the grid and proceed to next verification
    
    uy += square_size                                            #we add square size because after being at that point, the turtle draws a cell upward
    ly = uy - (square_size * lines)
    if x <= (square_size * columns) + lx and x >= lx :           #ensure that we are within the boundaries of the grid
        if ly <= y and y <= uy:

            x = abs(lx - x)
            y = abs(ly - y)

            x_pos = int(x//square_size)         #to know position of the cell
            y_pos = int(y//square_size)

            i = lines - 1 - y_pos                #to get the index of the cell's value in the grid
            j = x_pos

            #print('x position', x_pos, 'and y position', y_pos)
            #square = grid[i][j]
            #print('The square is', square)

            grid[i][j] = 1                      #change the clicked cell to alive
    

def init():
#this function begins the program execution

    def get_inputs():
        shape = input('Enter [S] for a square and [R] for a rectangular canvas: ').upper()
        if shape == 'S':
            try:
                array_size = int(input('Select dimension: '))
                square_size = int(input('Enter square size: '))
                return [array_size, array_size, square_size]
            except:
                get_inputs()

        elif shape == 'R': 
            try:
                lines = int(input('Enter number of lines: '))
                columns = int(input('Enter number of columns: '))
                square_size = int(input('Enter square size: '))
                return [lines, columns, square_size]
            except:
                get_inputs()

        else: get_inputs()

    if len(sys.argv) >= 3:
        try:
            lines = int(sys.argv[1])
            columns = int(sys.argv[2])
            square_size = int(sys.argv[3])                            

        except:
            try:
                lines = columns = int(sys.argv[1])
                square_size = int(sys.argv[2])

            except:   
                information = get_inputs()
                lines = information[0]
                columns = information[1]
                square_size = information[2]

    else: 
          information = get_inputs()
          lines = information[0]
          columns = information[1]
          square_size = information[2]

    grid = create_array(lines, columns)
    
    #gap = square_size/size 
    #if gap < 1: gap **= -1      #to take the dividend of both values
    #elif gap == 1: gap = 5      #take an arbitray value
    gap = 10 ##
    
    boundaries = setup_screen()

    while True:
        grid = decide(grid, lines, columns)
        turtle.onscreenclick(lambda x, y: update_grid(x, y, grid, lines, columns, square_size, boundaries[0], boundaries[1]))
        turtle.listen()
        draw(grid, square_size, lines, columns, gap)

init()