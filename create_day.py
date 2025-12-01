#!/usr/bin/env python3
"""Helper script to create a new day directory structure."""

import sys
from pathlib import Path


def create_day(day_number: int):
    """Create directory structure for a new day."""
    day_dir = Path(__file__).parent / "solutions" / f"day{day_number:02d}"
    
    if day_dir.exists():
        print(f"Day {day_number:02d} already exists!")
        return
    
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # Create template files
    part1_template = f'''"""Advent of Code 2025 - Day {day_number}, Part 1"""

from pathlib import Path


def main():
    # Get the input file path (relative to this script)
    input_path = Path(__file__).parent / "input.txt"
    
    # Read input
    with open(input_path) as f:
        data = f.read().strip()
    
    # TODO: Implement your solution here
    print(f"Part 1 solution: {{data}}")


if __name__ == "__main__":
    main()
'''
    
    part2_template = f'''"""Advent of Code 2025 - Day {day_number}, Part 2"""

from pathlib import Path


def main():
    # Get the input file path (relative to this script)
    input_path = Path(__file__).parent / "input.txt"
    
    # Read input
    with open(input_path) as f:
        data = f.read().strip()
    
    # TODO: Implement your solution here
    print(f"Part 2 solution: {{data}}")


if __name__ == "__main__":
    main()
'''
    
    (day_dir / "part1.py").write_text(part1_template)
    (day_dir / "part2.py").write_text(part2_template)
    (day_dir / "input.txt").write_text("# Paste your puzzle input here\n")
    
    print(f"Created day {day_number:02d} structure at {day_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_day.py <day_number>")
        print("Example: python create_day.py 2")
        sys.exit(1)
    
    try:
        day_num = int(sys.argv[1])
        if day_num < 1 or day_num > 25:
            print("Day number must be between 1 and 25")
            sys.exit(1)
        create_day(day_num)
    except ValueError:
        print("Day number must be an integer")
        sys.exit(1)

