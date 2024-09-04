#!/usr/bin/python3
"""module for a prime game"""


def isWinner(x, nums):
    "method for the prime game"
    def prime_list(n):
        """method to generate a prime number list"""
        p_list = [True] * (n + 1)
        p_list[0] = p_list[1] = False
        for start in range(2, int(n**0.5) + 1):
            if p_list[start]:
                for i in range(start * start, n + 1, start):
                    p_list[i] = False
        return p_list

    maria_score = 0
    ben_score = 0

    for n in nums:
        p_list = prime_list[n]
        primes = [i for i in range(2, n + 1) if p_list[i]]
        
        count = len(primes)
        
        if count % 2 == 1:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None
