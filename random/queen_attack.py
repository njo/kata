#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Build the board and convert from 1 based at the bottom to 0 based up top
    board = [[0 for _ in range(n)] for _ in range(n)]
    for row, col in obstacles:
        col -= 1
        row = n - row
        board[row][col] = 1

    def can_see(pos, direction, total):
        # travel in the direction from current pos
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])

        # check out of bounds
        if new_pos[1] < 0 or new_pos[1] >= n or new_pos[0] < 0 or new_pos[0] >= n:
            return total

        if board[new_pos[1]][new_pos[0]] == 1:
            return total

        return can_see(new_pos, direction, total + 1)
    
    queen_start = (n - r_q, c_q - 1)
    total_squares = 0

    for dirs in [(+1, 0), (-1, 0), (0, +1), (0, -1), (+1, +1), (-1, +1), (+1, -1), (-1, -1)]:
        total_squares += can_see(queen_start, dirs, 0)

    return total_squares

if __name__ == '__main__':
    assert queensAttack(4, 0, 4, 4, []) == 9
    assert queensAttack(8, 0, 4, 4, [(3, 5)]) == 24
