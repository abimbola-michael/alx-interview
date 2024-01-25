#!/usr/bin/env python3
"""
Write a script that reads stdin line by line and computes metrics:"""

import sys


def print_stats(status_codes, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def main():
    """
    Reads stdin line by line and computes metrics:
    """
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            words = line.strip().split(" ")
            if len(words) > 4:
                file_size = int(words[-1])
                status_code = words[-2]
                if status_code in status_codes.keys():
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1
            
            if line_count % 10 == 0:
                print_stats(status_codes, total_size)
    except KeyboardInterrupt:
        print_stats(status_codes, total_size)


if __name__ == "__main__":
    main()
