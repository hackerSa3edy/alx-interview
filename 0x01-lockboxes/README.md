# Lockboxes Algorithm

This project contains an implementation of an algorithm to determine if all lockboxes can be unlocked. The algorithm is implemented in Python and is located in the `0-lockboxes.py` file.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Function](#function)
  - [`canUnlockAll`](#canunlockall)
- [Examples](#examples)

## Overview

The lockboxes problem is a classic algorithmic challenge where you are given a list of boxes, each containing a list of keys. Each key can open another box. The goal is to determine if you can open all the boxes starting from the first box (box 0).

## Usage

To use the function provided in this project, you need to have Python installed on your system. You can run the function by importing it into your Python script or by running the `0-lockboxes.py` file directly.

## Function

### `canUnlockAll`

The `canUnlockAll` function uses a breadth-first search (BFS) approach to determine if all boxes can be unlocked. It starts with the first box and explores all reachable boxes using a queue.

#### Parameters

- `boxes` (list of list of int): A list where each element is a list of keys contained in that box. The keys are represented by integers, where each integer is the index of another box.

#### Returns

- `bool`: True if all boxes can be unlocked, False otherwise.

## Examples

Here are some examples of how to use the function:

```python
from 0-lockboxes import canUnlockAll

boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2, 3], [], [4], [5], []]
print(canUnlockAll(boxes))  # Output: False
```
