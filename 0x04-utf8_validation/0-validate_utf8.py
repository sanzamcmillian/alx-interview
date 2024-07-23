#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """method that determines if data set represents a valid UTF-8 encoding"""
    def get_num_bytes(byte):
        """Check the number of leading 1s in the first byte"""
        if (byte >> 5) == 0b110:
            return 2
        elif (byte >> 4) == 0b1110:
            return 3
        elif (byte >> 3) == 0b11110:
            return 4
        elif (byte >> 7) == 0:
            return 1
        return -1

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])
        if num_bytes == -1 or i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if (data[i + j] >> 6) != 0b10:
                return False

        i += num_bytes

    return True
