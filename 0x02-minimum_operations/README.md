# Project: 0x02. Minimum Operations

## Tasks

| Task                  | File                                       |
| --------------------- | ------------------------------------------ |
| 0. Minimum Operations | [0-minoperations.py](./0-minoperations.py) |

## Overview

This project contains an implementation of an algorithm to determine the minimum number of operations required to print exactly `n` 'H' characters in a file. The allowed operations are:

1. Copy All: Copy all the characters present in the file.
2. Paste: Paste the characters that were copied.

The algorithm is implemented in Python and is located in the `0-minoperations.py` file.

## Usage

To use the function provided in this project, you need to have Python installed on your system. You can run the function by importing it into your Python script or by running the `0-main.py` file directly.

## Function

### `minOperations`

The `minOperations` function uses prime factorization to determine the minimum number of operations needed to print exactly `n` 'H' characters in a file.

#### Parameters

- `n` (int): The number of 'H' characters to be printed.

#### Returns

- `int`: The minimum number of operations required to print `n` 'H' characters. Returns 0 if `n` is less than or equal to 1.

## Examples

Here are some examples of how to use the function:

```python
from 0-minoperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min # of operations to reach 4 char: 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
# Output: Min # of operations to reach 12 char: 7
```

You can also run the `0-main.py` file to see the function in action:

```sh
python3

0-main.py
```
