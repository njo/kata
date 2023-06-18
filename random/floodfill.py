#  http://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/

"""Given a 2D array and a coordinate and a 'color', implement 'flood fill'. Flood fill colors everything with the same color as the given coordinate with 'color' (similar to the bucket fill in Microsoft paint)

Input:
       screen[M][N] = [[1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0],
                      [1, 0, 0, 1, 1, 0, 1, 1],
                      [1, 2, 2, 2, 2, 0, 1, 0],
                      [1, 1, 1, 2, 2, 0, 1, 0],
                      [1, 1, 1, 2, 2, 2, 2, 0],
                      [1, 1, 1, 1, 1, 2, 1, 1],
                      [1, 1, 1, 1, 1, 2, 2, 1],
                      ];
    x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that
should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
       screen[M][N] = [[1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0],
                      [1, 0, 0, 1, 1, 0, 1, 1],
                      [1, 3, 3, 3, 3, 0, 1, 0],
                      [1, 1, 1, 3, 3, 0, 1, 0],
                      [1, 1, 1, 3, 3, 3, 3, 0],
                      [1, 1, 1, 1, 1, 3, 1, 1],
                      [1, 1, 1, 1, 1, 3, 3, 1],
                      ];
"""


def floodfill(grid, x, y, colour):
    """
    @param grid: List[List[int]]
    @param x: int
    @param y: int
    @param colour: int
    @return List[List[int]]
    """
    stack = []
    visited = {}
    size = len(grid)
    stack.append((x, y))
    initial = grid[y][x]

    while stack:
        x, y = stack.pop()
        visited[(x, y)] = True
        # If it's not the same colour as our initial we can ignore it
        if grid[y][x] != initial:
            continue
        grid[y][x] = colour

        for x1, y1 in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if x1 < 0 or y1 < 0 or x1 >= size or y1 >= size:  # it's out of bounds
                continue
            if (x1, y1) in visited:     # we've seen this before
                continue
            stack.append((x1, y1))

    return grid


initial = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1]]

final = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 3, 3, 3, 3, 0, 1, 0],
    [1, 1, 1, 3, 3, 0, 1, 0],
    [1, 1, 1, 3, 3, 3, 3, 0],
    [1, 1, 1, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 1, 3, 3, 1]]

result = floodfill(initial, 4, 4, 3)

assert(result == final)

print "Done!"
