interview technocal question 
Task

0. Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

Explanation:
The unlocker function is a recursive function that takes a box, the set of openboxes, and the list of boxes. It aims to unlock all the boxes recursively by exploring the contents of each box and adding any new boxes found to the set of open boxes. It returns the set of open boxes.
The canUnlockAll function is the main function that checks if all the boxes can be unlocked. It starts with the first box (box 0) already open. If there is only one box in the list, it is considered already unlocked, and the function returns True immediately. Otherwise, it calls the unlocker function to unlock the boxes recursively, passing the contents of the first box, the set of open boxes, and the list of boxes. If the number of open boxes is equal to the total number of boxes, it means all boxes can be unlocked, and the function returns True. Otherwise, it returns False.
