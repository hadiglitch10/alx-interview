#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = [0]   # Use a list as a queue to manage the boxes we can visit

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
