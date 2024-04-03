#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, side_length):
        """Initialize the Square with a given side length."""
        self.side_length = side_length

    def area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.side_length

if __name__ == "__main__":
    # Example usage
    square = Square(5)
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())
