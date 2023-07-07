#!/usr/bin/env python3

"""
lock-boxes
"""
def unlocker(box, openboxes, boxes):
    """Recursive function to unlock the boxes"""
    if len(boxes) == len(openboxes):
        # If all boxes are already open, return the set of open boxes
        return openboxes
    for value in box:
        if value >= len(boxes):
            continue
        if value not in openboxes:
            # If the box is not already open, add it to the set of open boxes
            openboxes.add(value)
            # Recursively call the unlocker function for the next box
            unlocker(boxes[value], openboxes, boxes)
    return openboxes


def canUnlockAll(boxes):
    # Main function to check if all boxes can be unlocked
    openboxes = {0}  # Start with the first box open
    if len(boxes) == 1:
        # If there is only one box, it is already unlocked
        return True
    unlocked = unlocker(boxes[0], openboxes, boxes)
    if len(unlocked) == len(boxes):
        # If the number of open boxes is equal to the total number of boxes, return True
        return True
    else:
        # Otherwise, return False
        return False
