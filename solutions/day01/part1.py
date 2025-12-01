"""Advent of Code 2025 - Day 1, Part 1: Secret Entrance

The dial has positions 0-99 and starts at position 50.
Instructions are 'L' or 'R' followed by a number of clicks.
Find the final position after executing all instructions.
"""

from pathlib import Path
import re


def is_valid_instruction(line: str) -> bool:
    """Check if a line is a valid instruction (L or R followed by digits)."""
    return bool(re.match(r'^[LR]\d+$', line.strip()))


def parse_instruction(instruction: str) -> tuple[str, int]:
    """Parse an instruction into direction and steps."""
    direction = instruction[0]
    steps = int(instruction[1:])
    return direction, steps


def main():
    # Get the input file path (relative to this script)
    input_path = Path(__file__).parent / "input.txt"
    
    # Read input and filter to only valid instructions
    with open(input_path) as f:
        instructions = [
            line.strip() for line in f 
            if line.strip() and is_valid_instruction(line)
        ]
    
    # Start at position 50
    position = 50
    
    # Execute all instructions
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        
        if direction == 'R':
            # Rotate right: add steps and wrap around
            position = (position + steps) % 100
        elif direction == 'L':
            # Rotate left: subtract steps and wrap around
            position = (position - steps) % 100
    
    print(f"Part 1: Final position is {position}")


if __name__ == "__main__":
    main()

