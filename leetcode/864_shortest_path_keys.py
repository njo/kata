from typing import List
import string

LOCKS = string.ascii_uppercase
KEYS = string.ascii_lowercase
PLAYER = "@"
WALL = "#"
EMPTY = "."

class Solution:
    least = None

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        player = None
        keycount = 0
        # Find player starting position
        # Count number of keys
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col in KEYS:
                    keycount += 1
                elif col == PLAYER:
                    player = (x, y)

        if keycount == 0:
            return 0

        if player is None:
            return -1

        def recurse(player, visited, keys, steps):
            if self.least and steps >= self.least:    # early exit if we won't beat the best
                return None
            x, y = player
            # check it's a valid move
            # is it in bounds
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
                return None

            # is it a new tile
            if player in visited:
                return None

            tile = grid[y][x]

            # do we have the key
            if tile in LOCKS:
                if tile.lower() not in keys:
                    return None
            elif tile == WALL:
                return None

            # valid move
            visited.add(player)
            #print(tile, player)

            # check for win
            if tile in KEYS and not tile in keys:
                keylist = [k for k in keys]
                keylist.append(tile)
                keys = "".join(sorted(keylist))
                if len(keys) == keycount:
                    return steps
                visited = set([player]) # where we found this key is the new history

            # try travel in the directions
            directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            results = [recurse(direction, visited.copy(), keys, steps + 1) for direction in directions]
            results = [r for r in results if r is not None]
            result = None if len(results) == 0 else min(results)
            if result:
                self.least = min(result, self.least) if self.least else result
            return result

        result = recurse(player, set(), "", 0)
        return -1 if not result else result

assert Solution().shortestPathAllKeys(["b","A","a","@","B"]) == 3
# assert Solution().shortestPathAllKeys([
#     "@...a",
#     ".###A",
#     "b.BCc"]
# ) == 10
# assert Solution().shortestPathAllKeys([
#     "@.a..",
#     "###.#",
#     "b.A.B"]) == 8
assert Solution().shortestPathAllKeys([
    "@..aA",
    "..B#.",
    "....b"]) == 6
assert Solution().shortestPathAllKeys(["@Aa"]) == -1
