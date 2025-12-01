"""Advent of Code 2025 - Day 1, Part 2: Secret Entrance

Count how many times the dial ends pointing at position 0 after any rotation.
The actual password is the number of times the dial is left pointing at 0 after any rotation.
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
    times_at_zero = 0
    
    # Execute all instructions and count how many times we end at position 0
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        
        if direction == 'R':
            # Rotate right
            position = (position + steps) % 100
        elif direction == 'L':
            # Rotate left
            position = (position - steps) % 100
        
        # Count if the dial ends pointing at 0 after this rotation
        if position == 0:
            times_at_zero += 1
    
    print(f"Part 2: Number of times dial ends at 0 (password) is {times_at_zero}")


if __name__ == "__main__":
    main()

