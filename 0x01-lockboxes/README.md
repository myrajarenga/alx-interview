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

The function canUnlockAll takes a list of boxes as input.
num_boxes stores the total number of boxes.
unlocked_boxes is a list that keeps track of whether each box is unlocked or not. Initially, all boxes are set to False except the first box, which is set to True since it's unlocked.
The keys_stack variable is used to store the keys that we currently have. It starts with the keys in the first box.
The while loop iterates as long as there are keys in the stack.
In each iteration, we take a key from the stack (current_key) and check if it's a valid key and if it can unlock a box.
If the key is valid and can unlock a box, we mark the corresponding box as unlocked in the unlocked_boxes list and add the keys inside that box to the keys_stack.
After the loop finishes, we use the all function to check if all boxes are unlocked (True in unlocked_boxes).
The function returns True if all boxes are unlocked, indicating that all boxes can be unlocked. Otherwise, it returns False.
