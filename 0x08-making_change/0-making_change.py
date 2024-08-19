#!/usr/bin/python3
"""Module to compute change"""


def makeChange(coins, total):
    """Method to calculate change"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    new_ans = 0
    for i in range(len(coins)):
        change = total // coins[i]
        if change > 0 and total > 0:
            total = total - (coins[i] * change)
            new_ans = new_ans + change
    if total == 0:
        return new_ans
    else:
        return -1
