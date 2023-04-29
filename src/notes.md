# John Conway's The Game of Life

## Constituents;
    It consists of squares in a space (grid) sometimes refered to as cells
    Contains cells with are either on/off, alive/dead

## Rules;

### Death/alive
        If a cell has no alive neighbour, it dies
        If a cell has only on alive neighbour, it dies
        But if it has two alive neighbours, it remains alive
        Any live cell with more than three live neighbours dies, as if by overpopulation

### Birth
        If a dead cell has exactly three alive neighbours, it will be born (springs to life)
        Note: A stable pattern is seen when each of cells have an equi-number of alive neighbours

## Glider
    It is observed from as movement of cells
    Which is actually the movement of the pattern of quality(black/white) which can be seen as energy
    Note: Because of it's invariance (but it shapes repeats every give cycle) it seems to have it's own existence

### Other shapes
    Shapes such as ships, loafs, blocks, brain and boats are also observed


## Matrix representation
    Viewing a 3x3 matrix representation, we have 9 digits (binaty numbers) giving us 12 possible combinations
    Viewing a 4x4 matrix representation, we have 16 digit binaty numbers giving us about 65000 possible combinations

    Note: The complexity of the algorithm is very high

