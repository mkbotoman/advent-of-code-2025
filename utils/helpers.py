"""Common helper functions for Advent of Code solutions."""

from pathlib import Path


def read_input(day: int, filename: str = "input.txt") -> str:
    """
    Read input file for a given day.
    
    Args:
        day: Day number (e.g., 1 for day01)
        filename: Name of the input file (default: input.txt)
    
    Returns:
        Contents of the input file as a string
    """
    input_path = Path(__file__).parent.parent / "solutions" / f"day{day:02d}" / filename
    return input_path.read_text().strip()


def read_input_lines(day: int, filename: str = "input.txt") -> list[str]:
    """
    Read input file for a given day, returning lines as a list.
    
    Args:
        day: Day number (e.g., 1 for day01)
        filename: Name of the input file (default: input.txt)
    
    Returns:
        List of lines from the input file
    """
    return read_input(day, filename).splitlines()

