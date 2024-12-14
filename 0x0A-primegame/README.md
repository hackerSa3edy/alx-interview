# 0x0A. Prime Game

## Description

This project implements a prime number game where Maria and Ben take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The player that cannot make a move loses the game.

## Game Rules

1. Maria and Ben take turns playing
2. Maria always goes first
3. Each player takes turns picking a prime number from the set of remaining numbers
4. Once a prime number is chosen, that number and its multiples are removed from the set
5. The player that cannot make a move loses the game
6. The game is repeated x times

## Implementation

### Function: `isWinner(x, nums)`

#### Parameters

- `x`: Number of rounds
- `nums`: Array of n values for each round

#### Returns

- Name of the player that won the most rounds
- If the winner cannot be determined, returns None

#### Algorithm

1. Uses Sieve of Eratosthenes to efficiently generate prime numbers
2. For each round:
   - Creates a list of prime numbers up to n
   - Counts the number of available prime numbers
   - If count is even, Ben wins the round
   - If count is odd, Maria wins the round
3. Compares total wins to determine the overall winner

## Example Usage

```python
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: Ben
```

## Requirements

- Python 3.4.3 or higher
- All files should end with a new line
- First line of all files should be `#!/usr/bin/python3`
- PEP 8 style compliance
- All modules should have documentation
- All functions should have documentation
