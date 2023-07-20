#!/usr/bin/python3
"""
script that reads stdin by line
"""


import sys
import re


def compute_and_print_stats(total_size=0, status_code_count=None, line_count=0):
    """function to computr statistics"""
    if status_code_count is None:
        status_code_count = {}

    try:
        for line in sys.stdin:
            match = re.match(
                r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)',
                line
            )

            if match:
                ip_address, date, status_code, file_size = match.groups()
                total_size += int(file_size)

                if status_code.isdigit():
                    status_code_count[int(status_code)] =\
                            status_code_count.get(int(status_code), 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_code_count)

        print("\nEnd of input. Final statistics:")
        print_statistics(total_size, status_code_count)

    except KeyboardInterrupt:
        """If interrupted by Ctrl + C, print the current statistics and exit"""
        print_statistics(total_size, status_code_count)
        sys.exit(0)


def print_statistics(total_size, status_code_count):
    """print total statistics"""
    print("File size:", total_size)
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")
    print()


if __name__ == "__main__":
    compute_and_print_stats()
