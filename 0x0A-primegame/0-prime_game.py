#!/usr/bin/python3
"""module for a prime game"""


def prime_list(n):
    """method generate a prime number list"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """method to generate a winner for the prime game"""
    p_list = []
    ben_score = 0
    maria_score = 0
    for i in range(x):
        n = list(range(1, nums[i] + 1))
        for j in range(len(n)):
            if (prime_list(n[j]) is not True):
                continue
            else:
                p_list.append(n[j])
        if len(p_list) % 2 == 0:
            ben_score += 1
            p_list.clear()
        else:
            maria_score += 1
            p_list.clear()
    if ben_score > maria_score:
        return 'Ben'
    elif maria_score > ben_score:
        return 'Maria'
    else:
        return None
