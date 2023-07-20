#!/usr/bin/python3
"""
script that reads stdin by line
"""


import sys
import re


def compute_metrics_recursive(total_size=0, status_code_count=None, line_count=1):
    """function to compute metix using recursion"""
    if status_code_count is None:
        status_code_count = {}

    try:
        line = next(sys.stdin)
    except StopIteration:
        print("\nEnd of input. Final statistics:")
        print_statistics(total_size, status_code_count)
        return

    match = re.match(
        r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)',
        line
    )

    if match:
        ip_address, date, status_code, file_size = match.groups()
        total_size += int(file_size)

        if status_code.isdigit():
            status_code_count[int(status_code)] = status_code_count.get(int(status_code), 0) + 1

    if line_count % 10 == 0:
        print_statistics(total_size, status_code_count)

    compute_metrics_recursive(total_size, status_code_count, line_count + 1)


def print_statistics(total_size, status_code_count):
    """print statistics"""
    print("Total file size:", total_size)
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")
    print()


if __name__ == "__main__":
    compute_metrics_recursive()
