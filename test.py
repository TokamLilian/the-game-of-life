from game_of_life import *

def test():
   
    def test_create_array():
        
        def create_grid1():
            lines = randint(1, 10)
            columns = randint(1, 10)

            grid = create_array(lines, columns)
            assert len(grid) == lines

            for i in range(lines):
                assert len(grid[i]) == columns

        create_grid1()

        def create_grid2():
            lines = randint(2, 10)
            columns = randint(2, 30)

            grid = create_array(lines, columns)
            assert len(grid)*len(grid[1]) == lines*columns 
        
        create_grid2()

        def create_grid3():
            lines = randint(1, 20)
            columns = randint(1, 20)
            grid = create_array(lines, columns)
            new_grid = create_array(lines, columns)

            assert grid != new_grid
        create_grid3()

    test_create_array()


    def test_decide():
         
        def test_decide1():
            grid = [ [0, 1, 1],
                     [1, 1, 1],
                     [0, 0, 0] ]

            assert decide(grid, len(grid), len(grid[0])) != grid

        test_decide1()

        def test_decide2():
            grid = [ [0, 0, 1],
                     [1, 0, 1],
                     [1, 0, 0] ]

            assert decide(grid, len(grid), len(grid[0])) == [ [0, 1, 0], [0, 1, 0], [0, 0, 0] ]

        test_decide2()

        def test_decide3():
            grid = create_array(4, 5)
            assert decide(grid, 4, 5) != grid

        test_decide3()

    test_decide()
        

    def test_get_neighbour():

        def test_get_neighbour1():
            lines = randint(2, 10)
            columns = randint(2, 30)

            grid = create_array(lines, columns)
            for i in range (lines*columns):
                neighbour = get_neighbour(grid, i, lines, columns)
                assert len(neighbour) <= 8
                assert len(neighbour) >= 3

        test_get_neighbour1()

        def test_get_neighbour2():
            grid = [ [0, 1, 1],
                     [1, 1, 1],
                     [0, 0, 0] ]
            
            assert get_neighbour(grid, 1, len(grid), len(grid[1])) == [0, 1, 1, 1, 1]
            assert get_neighbour(grid, 8, len(grid), len(grid[2])) == [0, 1, 1]
        
        test_get_neighbour2()

        def test_get_neighbour3():
            lines = randint(2, 30)
            columns = randint(2, 30)

            grid = create_array(lines, columns)
            last = (lines*columns) - 1

            assert len(get_neighbour(grid, last, len(grid), len(grid[2]))) == 3
            assert len(get_neighbour(grid, 0, len(grid), len(grid[2]))) == 3

        test_get_neighbour3()

    test_get_neighbour()


test()