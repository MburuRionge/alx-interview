#!/usr/bin/python3

"""N queens puzzle of placing N non attacking queens on a chessboard"""

import sys


class Nqueens:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ declaring global variables """
        self.n = n
        self.m = [0 for _ in range(n + 1)]
        self.res = []

    def chess(self, p, i):
        """
        checks if m queen can be placed in i column or in a row or diagonal
        """
        #checks from 1 to the previous queen(k - 1)
        for q in range(1, p):
            #there is already a queen in column or in same digonal
            if self.m[q] == i or abs(self.m[q] - i) == abs(q - p):
                return 0 
        return 1

    def queen(self, p):
        """tries to place every queen on the board"""
        # i goes from column 1 to column n(1st column is 1st index)
        for i in range(1, self.n + 1):
            if self.chess(p, i):
                # then place N queen in i column
                self.m[p] = i
                if p == self.n:
                    # a solution found when all 4 Queens were placed
                    solution = []
                    for row in range(1, self.n + 1):
                        solution.append([row - 1, self.m[row] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.queen(p + 1)
        return self.res

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
