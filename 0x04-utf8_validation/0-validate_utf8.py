#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """method that determines if data set represents a valid UTF-8 encoding"""
    for i in data:
        if i > 0 and i <= 128:
            return True
        return False
