##Learning UTF-8 Validation

Taks
0. Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer


How  I solved this qn
The function iterates through the list to validate the UTF-8 encoding.
function takes a bytes object (data) as input and iterates through the bytes to validate the UTF-8 encoding. It returns True if the sequence is valid UTF-8 and False otherwise. I use  a for loop to iterate and condtional if and esle statements to get the desired outputs

