#this the test file for the main program
from game_of_life import *

def test():
    
    def test_decide():
        grid = [ [0, 0, 1],
                 [0, 1, 1],
                 [0, 0, 0] ]

        decide(grid)

    test_decide()


test()