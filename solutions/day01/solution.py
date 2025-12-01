"""Advent of Code 2025 - Day 1: Secret Entrance

The dial has positions 0-99 and starts at position 50.
Instructions are 'L' or 'R' followed by a number of clicks.

Part 1: Find the final position after executing all instructions.
Part 2 (original): Count how many times dial ends at position 0 after any rotation.
Part 2 (method 0x434C49434B): Count ALL times the dial points at 0, including during rotations.
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


def part1(instructions: list[str]) -> int:
    """Solve Part 1: Find final position."""
    position = 50
    
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        
        if direction == 'R':
            position = (position + steps) % 100
        elif direction == 'L':
            position = (position - steps) % 100
    
    return position


def part2(instructions: list[str]) -> int:
    """Solve Part 2: Count how many times dial ends at position 0."""
    position = 50
    times_at_zero = 0
    
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        
        if direction == 'R':
            position = (position + steps) % 100
        elif direction == 'L':
            position = (position - steps) % 100
        
        # Count if the dial ends pointing at 0 after this rotation
        if position == 0:
            times_at_zero += 1
    
    return times_at_zero


def part2_method_click(instructions: list[str]) -> int:
    """Solve Part 2 using method 0x434C49434B: Count ALL times dial points at 0.
    
    Count every time the dial points at 0 during rotations.
    Important: Don't double-count - if we start at 0, don't count it (it was already
    counted as the end of the previous rotation if applicable).
    """
    position = 50
    times_at_zero = 0
    
    for instruction in instructions:
        direction, steps = parse_instruction(instruction)
        start_pos = position
        
        if direction == 'R':
            # Rotate right: positions visited are start_pos, start_pos+1, ..., start_pos+steps
            # Count how many of these are 0 mod 100, but exclude the starting position
            end_pos_raw = start_pos + steps
            
            # Count multiples of 100 in (start_pos, start_pos+steps] (exclude start)
            start_mult = start_pos // 100
            end_mult = end_pos_raw // 100
            
            # Count multiples of 100 in the range, excluding start_pos
            if start_pos % 100 == 0:
                # Start at 0, but don't count it (already counted as end of prev rotation if applicable)
                # Count all multiples of 100 in (start_pos, start_pos+steps]
                # This is end_mult - start_mult (all multiples in range, excluding start)
                times_at_zero += end_mult - start_mult
            else:
                # Count all multiples in range
                times_at_zero += end_mult - start_mult
            
            position = end_pos_raw % 100
            
        elif direction == 'L':
            # Rotate left: positions visited are start_pos, start_pos-1, ..., start_pos-steps
            # Count how many of these are 0 mod 100, but exclude the starting position
            end_pos_raw = start_pos - steps
            
            # Don't count starting position (already counted if it was end of prev rotation)
            
            # Count backwards crossings
            if end_pos_raw < 0:
                # Wrap backwards: cross 0, -100, -200, etc.
                abs_end = abs(end_pos_raw)
                if start_pos > 0:
                    # Cross 0 once going from positive to negative, then additional multiples
                    times_at_zero += 1 + (abs_end // 100)
                else:
                    # Started at 0, don't count it, just count additional multiples
                    times_at_zero += abs_end // 100
            elif end_pos_raw % 100 == 0:
                # End at 0
                if start_pos % 100 != 0:
                    # Didn't start at 0, so count ending at 0
                    times_at_zero += 1
            
            position = end_pos_raw % 100
    
    return times_at_zero


def main():
    # Get the input file path (relative to this script)
    input_path = Path(__file__).parent / "input.txt"
    
    # Read input and filter to only valid instructions
    with open(input_path) as f:
        instructions = [
            line.strip() for line in f 
            if line.strip() and is_valid_instruction(line)
        ]
    
    # Solve all parts
    result1 = part1(instructions)
    result2_original = part2(instructions)
    result2_click = part2_method_click(instructions)
    
    print(f"Part 1: Final position is {result1}")
    print(f"Part 2 (original): Number of times dial ends at 0 is {result2_original}")
    print(f"Part 2 (method 0x434C49434B): Number of times dial points at 0 (password) is {result2_click}")


if __name__ == "__main__":
    main()

