#!/usr/bin/python3
"""Lockboxes Algorithm

This module provides a function to determine if all lockboxes can be unlocked.
Each box may contain keys to other boxes, and the goal is to check if all boxes
can be opened starting from the first box (box 0).
"""


def canUnlockAll(boxes):
    """Function to determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each element is a list of
        keys contained in that box. The keys are represented by integers,
        where each integer is the index of another box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    The function uses a Breadth-First Search (BFS) approach to explore all
    reachable boxes starting from the first box. It maintains a list of opened
    boxes and a queue of boxes to be processed. For each box, it marks all
    reachable boxes as opened and adds them to the queue. The function returns
    True if all boxes are opened, otherwise it returns False.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
