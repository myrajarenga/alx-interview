#!/usr/bin/python3
"""
script that reads stdin by line
"""

import sys


def compute_metrics():
    code = {}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()

            if not line:
                """If the line is empty"""
                print_statistics(code, file_size)
                return

            """Split the line using double quotes as the separator"""
            parts = line.split('"')

            if len(parts) >= 3:
                """Extract the file size from the last part"""
                size = int(parts[-1].split()[-1])
                file_size += size

                """Extract the status code from the middle part"""
                status_code = parts[1].split()[-2]

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
