#Log parsing technical interview question

Task
0. logparsing
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order


Explanation
We begin by importing the sys module to access the standard input and output streams.
The status_codes_dict is a dictionary that will be used to store the count of each status code encountered in the input. All the status codes are initialized to zero.
total_size is initialized to zero to keep track of the cumulative file size encountered in the input.
count is initialized to zero to keep track of the number of lines counted so far.

Before starting the input processing, the code prints the initial statistics. This includes the initial total_size and the counts of each status code that has a non-zero count. The counts are printed in ascending order of the status codes.

The code uses a try-except block to catch any exceptions that may occur during input processing. 
However, it uses a broad Exception  to catch  exceptions to handle them accordingly.
The code enters a loop to read lines from the standard input (sys.stdin).
Each line is split into words using split(" "). If the line has more than 4 elements (meaning it meets the specified input format), the code proceeds to extract the status code and file size.
If the status code received exists in the status_codes_dict, its count is incremented.
The total_size is updated by adding the file size of the current line.
The count is incremented to keep track of the number of lines processed.
If count reaches 10 (i.e., every 10 lines), it resets count to zero, prints the current total_size, and then prints out the counts of each status code in ascending order (skipping codes with count 0).

The finally block ensures that the final statistics (total size and status code counts) are printed, even if an exception occurred during the input processing.
In summary, the code reads lines from the standard input and processes them according to the specified format. It keeps track of the total file size and counts of each status code encountered. It prints statistics every ten lines and displays the final statistics at the end of input processing.
