#!/usr/bin/python3
"""
script that reads stdin by line
"""

import sys
import re


def compute_metrics():
    code = {}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            match = re.match(
                r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)',
                line
            )

            if match:
                _, _, status_code, size = match.groups()
                file_size += int(size)

                code[status_code] = code.get(status_code, 0) + 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(code, file_size)

    except KeyboardInterrupt:
        print_statistics(code, file_size)


def print_statistics(code, file_size):
    print("file size:", file_size)
    for status_code, count in sorted(code.items()):
        print(f"{status_code}: {count}")
    print()


if __name__ == "__main__":
    compute_metrics()
