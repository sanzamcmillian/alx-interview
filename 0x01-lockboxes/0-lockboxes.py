#!/usr/bin/python3
"""Unlock boxes using n keys from the boxes"""


def canUnlockAll(boxes):
    """function that determines if all boxes can be opened
        Args:
            boxes(list): list of list, the boxes.
    """
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key < n and key not in unlocked:
                    queue.append(key)

    return len(unlocked) == n
