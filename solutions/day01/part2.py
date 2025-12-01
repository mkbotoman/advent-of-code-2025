"""Advent of Code 2025 - Day 1, Part 2"""

from pathlib import Path


def main():
    # Get the input file path (relative to this script)
    input_path = Path(__file__).parent / "input.txt"
    
    # Read input
    with open(input_path) as f:
        data = f.read().strip()
    
    # TODO: Implement your solution here
    print(f"Part 2 solution: {data}")


if __name__ == "__main__":
    main()

