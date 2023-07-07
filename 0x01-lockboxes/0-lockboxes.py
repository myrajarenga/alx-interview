#!/usr/bin/python3

"""
lock-boxes
"""


def unlocker(box, openboxes, boxes):
    """Recursive function to unlock the boxes"""
    if len(boxes) == len(openboxes):
        return openboxes
    for value in box:
        if value >= len(boxes):
            continue
        if value not in openboxes:
            openboxes.add(value)
            unlocker(boxes[value], openboxes, boxes)
    return openboxes


def canUnlockAll(boxes):
    """ Main function to check if all boxes can be unlocked"""
    openboxes = {0}
    if len(boxes) == 1:
        return True
    unlocked = unlocker(boxes[0], openboxes, boxes)
    if len(unlocked) == len(boxes):
        return True
    else:
        return False
