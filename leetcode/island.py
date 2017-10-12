"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

def find_count(grid):
    islands = 0
    seen = set()

    def find_rest_of_the_island(x, y):
        if (x, y) in seen:
            return

        seen.add((x, y))

        if grid[y][x] != "1":
            return

        if len(grid[y]) > x + 1:
            find_rest_of_the_island(x + 1, y)

        if x - 1 >= 0:
            find_rest_of_the_island(x - 1, y)

        if y - 1 >= 0:
            find_rest_of_the_island(x, y - 1)

        if len(grid) > y + 1:
            find_rest_of_the_island(x, y + 1)

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if (x, y) in seen:
                continue

            if tile == "0":
                seen.add((x, y))

            if tile == "1":
                islands += 1
                find_rest_of_the_island(x, y)

    return islands


example = [ "11110",
            "11010",
            "11000",
            "00000"]

example1 = ["11000",
            "11000",
            "00100",
            "00011"]

example2 = ["01010",
            "00111",
            "10010",
            "01100",
            "10101"]

for grid, expected in [(example, 1), (example1, 3), (example2, 6)]:
    assert(expected == find_count(grid))

print "Done"
