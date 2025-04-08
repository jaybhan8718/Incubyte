# String Calculator TDD

A basic Python implementation of a string calculator that supports custom delimiters, handles newlines, and raises errors for negative numbers.

## Features

- Handles empty strings
- Supports default delimiters: `,`, `\n`, and `|`
- Supports single-character custom delimiters (e.g., `\;\n1;2;3`)
- Detects and raises an error for negative numbers

## Usage

```python
from calculator import add

print(add("1,2"))          # Output: 3
print(add("1\n2,3"))       # Output: 6
print(add("\\;\n1;2;3"))   # Output: 6
