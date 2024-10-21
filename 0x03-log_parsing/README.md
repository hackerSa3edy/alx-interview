# Project: 0x03. Log Parsing

## Tasks

| Task              | File                           |
| ----------------- | ------------------------------ |
| 0. Log Generator  | [0-generator.py](./0-generator.py) |
| 1. Log Statistics | [0-stats.py](./0-stats.py)         |

## Overview

This project contains scripts for generating and parsing logs. The log generator script creates random log entries, while the log statistics script processes these logs to extract useful information.

## Usage

To use the scripts provided in this project, you need to have Python installed on your system. You can run the scripts directly from the command line.

### Log Generator (`0-generator.py`)

This script generates random log entries and writes them to the standard output. Each log entry includes an IP address, a timestamp, an HTTP request, a status code, and a file size.

### Log Statistics (`0-stats.py`)

This script reads log entries from the standard input and calculates statistics. It prints the total number of requests and the count of each status code.

## Examples

Here are some examples of how to use the scripts:

```sh
# Generate logs and process them with the stats script
python3

0-generator.py | python3 0-stats.py
```
