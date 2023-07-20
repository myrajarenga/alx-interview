#!/usr/bin/python3
"""
script that reads stdin by line
"""

import sys


def compute_metrics():
    code = {}
    file_size = 0
    vals_total = 0

    try:
        print_status_codes(code, file_size)

        for line in sys.stdin:
            line = line.split()
            file_size += int(line[-1])
            status = line[-2]
            vals = list(code.values())
            vals_total = sum(vals)

            if status not in code:
                code[status] = 1
            else:
                code[status] += 1

            vals_total += 1

            if vals_total % 10 == 0:
                print_status_codes(code, file_size)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Current statistics:")
        print_status_codes(code, file_size)
        sys.exit(0)


def print_status_codes(code, file_size):
    print("File size:", file_size)
    for status, count in sorted(code.items()):
        print(f"{status}: {count}")
    print()


if __name__ == "__main__":
    compute_metrics()
