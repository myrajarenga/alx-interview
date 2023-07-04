#!/usr/bin/env python3


def canUnlockAll(boxes):
    """ function to unlock boxes"""
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is unlocked

    # Iterate through the keys and unlock the corresponding boxes
    keys_stack = boxes[0]  # Start with the keys in the first box
    while keys_stack:
        current_key = keys_stack.pop()  # Take a key from the stack

        # Check if the key is valid and can unlock a box
        if current_key < num_boxes and not unlocked_boxes[current_key]:
            unlocked_boxes[current_key] = True  # Unlock the box
            keys_stack.extend(boxes[current_key])  # Add the keys

    return all(unlocked_boxes)  # Check if all boxes are unlocked
