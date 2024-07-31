#!/usr/bin/python3
"""N-queens puzzle"""
import sys
N = sys.argv


def valid(N):
    """Function for input validation"""
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    if not N[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(N[1]) < 4:
        print("N must be at least 4")
        exit(1)
    N = int(N[1])
    return N


def nqueens(N, i=0, a=[], b=[], c=[]):
    """Method to implement N-queens puzzle"""
    n = valid(N)
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from nqueens(N, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(N):
    """Function to solve the N-queens puzzle"""
    k = []
    i = 0
    for solution in nqueens(N, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


solve(N)
