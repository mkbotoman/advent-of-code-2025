# Advent of Code 2025

Solutions for Advent of Code 2025 challenges in Python.

## Structure

```
.
├── solutions/          # Daily challenge solutions
│   └── day01/         # Day 1 solution
│       ├── part1.py   # Part 1 solution
│       ├── part2.py   # Part 2 solution
│       ├── solution.py # Combined solution (optional)
│       └── input.txt  # Puzzle input
├── utils/             # Shared utilities
└── README.md          # This file
```

## Usage

Each day has its own directory under `solutions/`:
- `part1.py` - Solution for part 1
- `part2.py` - Solution for part 2 (or combined in `solution.py`)
- `input.txt` - Your puzzle input

Run a solution:
```bash
python solutions/day01/part1.py
```

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Notes

- Copy your puzzle input to `solutions/dayXX/input.txt`
- Solutions should read from `input.txt` in the same directory
- Use `utils/` for shared helper functions

