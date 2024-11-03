#!/usr/bin/python3
"""
UTF-8 Validation module
This module provides functionality to validate whether a given data set
represents a valid UTF-8 encoding.

UTF-8 is a variable-width character encoding that can encode all possible
Unicode code points. It uses 1-4 bytes for each character, with specific
patterns for continuation bytes.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes of data

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise

    Rules for UTF-8 validation:
    * 1-byte character: starts with 0
    * 2-byte character: starts with 110
    * 3-byte character: starts with 1110
    * 4-byte character: starts with 11110
    * Continuation bytes start with 10
    """
    num_bytes_to_follow = 0
    for char in data:
        binary = format(char, '#010b')[-8:]
        if num_bytes_to_follow == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                num_bytes_to_follow = 1
            elif binary.startswith('1110'):
                num_bytes_to_follow = 2
            elif binary.startswith('11110'):
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not binary.startswith('10'):
                return False
            num_bytes_to_follow -= 1
    return num_bytes_to_follow == 0
