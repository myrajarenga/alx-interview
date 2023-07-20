#!/usr/bin/python3
"""
script that reads stdin by line
"""

import sys
import re


def compute_metrics_recursive(file_sizes=0, status_counts=None, line_count=0):
    """function to compute metrix using recursion"""
    if status_counts is None:
        status_counts = {}

    try:
        line = input().strip()  # Read a line from the standard input

        if not line:
            print_statistics(file_sizes, status_counts)
            return

        # Use regular expression to match the input format
        match = re.match(
            r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)',
            line
        )

        if match:
            _, _, status_code, file_size = match.groups()
            file_sizes += int(file_size)

            if status_code.isdigit():
                status_counts[int(status_code)]\
                        = status_counts.get(int(status_code), 0) + 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics(file_sizes, status_counts)

        compute_metrics_recursive(file_sizes, status_counts, line_count)

    except KeyboardInterrupt:
        """Program interrupted. Current statistics"""
        print_statistics(file_sizes, status_counts)
        sys.exit(0)


def print_statistics(file_sizes, status_counts):
    """total ststistics"""
    print("Total file size:", file_sizes)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")
    print()


if __name__ == "__main__":
    compute_metrics_recursive()
