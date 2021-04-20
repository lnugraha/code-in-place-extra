"""
Date: April 20, 2021
By: Leo Nugraha
Description: This program demosntrates how functions in Python work.
There are seven categories of functions that this file represents:
    1. Blank function
    2. Function that receives one input and returns one output
    3. Function that receives one input and returns more than one output
    4. Function that receives and returns more than one arguments
    5. Function with a default parameter input
    6. Function with more than one default parameter inputs
    7. Lambda notation (i.e., function without def declaration)
"""

import math

def blank_function():
    """
    1. Blank Function
    A function that neither receives an input nor generates an output requires
    pass keyword to be able to get called properly
    """
    pass

def square_area(side):
    """
    2. Function with one input and one output
    This function demonstrates how a function returns a processed output 
    based on the received input
    This function calculates the area of a square
    side: the side of the square, must be a positive number
    area: the output of the square, must be a psitive number
    """
    area = side * side
    return area

def rectangle_area(length, width):
    """
    3. Function with more than one inputs and one output
    This function demonstrates how a function returns an output
    based on the received inputs
    This function calculates the area of a square
    lendth: the length of the rectangle, must be a positive number
    width : the width of the rectangle, must be a positive number
    area  : the output of the square, must be a psitive number
    """
    area = length * width
    return area

def square_shape(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle_shape(length, width):
    area = length * width
    perimeter = 2 * (lenth + width)
    return area, perimeter

def square_default(side=5):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle_default(length=5, width=7):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


if __name__ == "__main__":
    # blank_function()
    


    # 7. Lambda Notation (in C++) / Closure in Swift
