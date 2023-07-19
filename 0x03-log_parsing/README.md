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
This script reads stdin line by line using a for loop and regular expressions to match the specified log format. It computes the total file size and counts the occurrences of each status code. After every 10 lines or when a keyboard interruption (CTRL + C) occurs, it calls the print_statistics function to print the metrics.
