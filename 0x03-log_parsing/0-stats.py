#!/usr/bin/python3
"""
script that reads stdin by line
"""


import sys
import re


def compute_metrics():
    """function to compuute metrix"""
    total_size = 0
    status_code_count = {}

    try:
        for line_count, line in enumerate(sys.stdin, start=1):
            """ Use regular expression to match the input format"""
            match = re.match(
                (r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" '
                 r'(\d{3}) (\d+)'),
                line
            )
            if match:
                ip_address, date, status_code, file_size = match.groups()
                total_size += int(file_size)

                if status_code.isdigit():
                    status_code_count[int(status_code)]\
                            = status_code_count.get(int(status_code), 0) + 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_code_count)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Final statistics:")
        print_statistics(total_size, status_code_count)


def print_statistics(total_size, status_code_count):
    """function to print statistics"""
    print("Total file size:", total_size)
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")
    print()


if __name__ == "__main__":
    compute_metrics()
