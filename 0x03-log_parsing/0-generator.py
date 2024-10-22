#!/usr/bin/python3
"""
Log Generator Script

This script generates random log entries and writes them to the
standard output.
Each log entry includes an IP address, a timestamp, an HTTP request, a status
code, and a file size.

Usage:
    python3 0-generator.py

The script runs indefinitely, generating log entries at random intervals.
"""

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write(
        "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n"
        .format(
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
            )
        )
    sys.stdout.flush()
