# Project: 0x05. N Queens

## Tasks

| Task              | File                           |
| ----------------- | ------------------------------ |
| 0. N Queens       | [0-nqueens.py](./0-nqueens.py) |

## Overview

This project contains an implementation of the N Queens problem solver. The N Queens problem is a classic algorithmic challenge where you need to place N non-attacking queens on an N×N chessboard.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable

## Usage

To use the function provided in this project, you need to have Python installed on your system. You can run the function by executing the `0-nqueens.py` file directly.

### Example

```sh
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
$
