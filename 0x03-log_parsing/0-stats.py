#!/usr/bin/python3
"""
Log Statistics Script

This script reads log entries from the standard input and calculates
statistics such as the total file size and the count of each
HTTP response code.

The script handles SIGINT (Ctrl+C) to gracefully print the statistics
before exiting.
"""

import re
import sys


def print_statistics(f_size, codes):
    """
    Prints the file size and HTTP status code counts.

    Args:
        f_size (int): The size of the file.
        codes (dict): A dictionary where keys are HTTP status codes (int) and
        values are the counts (int) of each status code.

    Returns:
        None
    """
    print("File size: {:d}".format(f_size))
    for key in sorted(codes.keys()):
        print("{:d}: {:d}".format(key, codes[key]))


def main():
    """
    Reads and processes log lines from standard input, updating file size and
    HTTP status code counts.
    Prints statistics every 10 lines and handles keyboard interruption
    gracefully.

    Args:
        None

    Returns:
        None
    """
    # Compile the regex pattern for matching log lines
    line_match = re.compile(
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "
        r"\"GET /projects/260 HTTP/1.1\" "
        r"(?P<resp_code>200|301|400|401|403|404|405|500) (?P<file_size>\d+)"
    )

    # Initialize counters
    f_size = 0
    codes = {}

    # Read and process log lines from standard input
    try:
        for i, line in enumerate(sys.stdin, 1):
            match = line_match.match(line.strip())
            if not match:
                continue

            # Update file size and response code counts
            f_size += int(match.group("file_size"))
            resp_code = int(match.group("resp_code"))
            codes[resp_code] = codes.setdefault(resp_code, 0) + 1

            # Print statistics every 10 lines
            if i % 10 == 0:
                print_statistics(f_size, codes)
        else:
            # Print final statistics if the loop exits normally
            if i % 10 != 0:
                print_statistics(f_size, codes)
    except KeyboardInterrupt:
        print_statistics(f_size, codes)
        raise


if __name__ == "__main__":
    """
    Entry point for the script. Calls the main function to start
    processing log lines.
    """
    main()
