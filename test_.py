#this the test file for the main program
from game_of_life import *

#global old_grid
def test():
    
    def test_decide1():
        old_grid = [ [0, 1, 1],
                 [1, 1, 1],
                 [0, 0, 0] ]

        decide(old_grid)

    #test_decide1()

    def test_decide2():
        old_grid = [ [0, 0, 1],
                     [1, 1, 1],
                     [1, 0, 0] ]

        decide(old_grid)

    #test_decide2()
    def test_draw():
        draw([ [1, 0, 1],
               [0, 1, 1],
               [1, 0, 0] ], 15)
        
    #test_draw()
    
    def test_play():
    
        #grid = [ [0, 0, 1],
        #         [1, 1, 1],
        #         [1, 0, 0] ]
        
        grid = [ [1, 1, 1, 0],
                 [0, 1, 0, 0],
                 [1, 0, 0, 1],
                 [1, 0, 1, 1] ]
        
        square_size, gap = 25, 2
        size = len(grid)
        
        boundaries = setup_screen(size, square_size, gap)

        while True:
            draw(grid, square_size, size, gap)
            turtle.onscreenclick(lambda x, y: update_grid(x, y, grid, size, square_size, boundaries[0], boundaries[1]))
            turtle.listen()

    #test_play()

    def test_create_array():
        lines = 4
        columns = 5
        grid = create_array(lines, columns)
        new = decide(grid, 25, lines, columns, 10)
    test_create_array()

test()