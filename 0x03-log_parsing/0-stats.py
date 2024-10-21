#!/usr/bin/python3
"""
Log Statistics Script

This script reads log entries from the standard input and calculates
statistics such as the total file size and the count of each
HTTP response code.

Usage:
    python3 0-stats.py

The script handles SIGINT (Ctrl+C) to gracefully print the statistics
before exiting.
"""

import regex
import signal
import sys

# Initialize the interrupt variable
interrupt = False


# Define the signal handler function
def sigint(*args):
    """
    Signal handler for SIGINT (Ctrl+C).
    Sets the interrupt variable to True to indicate that an interrupt
    was received.
    """
    global interrupt
    interrupt = True
    return None


# Set the signal handler for SIGINT
signal.signal(signal.SIGINT, sigint)

# Compile the regex pattern for matching log lines
line_match = regex.compile(
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "
    r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "
    r"\"GET /projects/260 HTTP/1.1\" "
    r"(?P<resp_code>200|301|400|401|403|404|405|500) (?P<file_size>\d+)"
)

# Initialize counters
cycle = 0
f_size = 0
codes = {}

# Read and process log lines from standard input
while line := sys.stdin.readline():
    match = line_match.match(line[:-1])
    if not match:
        continue

    # Update file size and response code counts
    f_size += int(match.group("file_size"))
    resp_code = int(match.group("resp_code"))
    codes.update({resp_code: codes.setdefault(resp_code, 0) + 1})

    # Print statistics every 10 lines or on interrupt
    if cycle == 9 or interrupt:
        print("File size: {:d}".format(f_size), flush=True)
        for key in sorted(codes.keys()):
            print("{:d}: {:d}".format(key, codes[key]), flush=True)

        # Reset counters
        codes.clear()
        f_size = 0
        cycle = -1
        if interrupt:
            raise KeyboardInterrupt

    cycle += 1
