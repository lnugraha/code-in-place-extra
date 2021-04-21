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
    area: the area of the square, must be a positive number
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
    area  : the area of the rectangle, must be a positive number
    """
    area = length * width
    return area

def square_shape(side):
    """
    4. Function with more than one outputs
    This function demonstrates how a function returns multiple outputs
    This function calculates the area and perimeter of a square
    area  : the area of the square, must be a positive number
    perimeter: the perimeter of the square, must be a positive number
    """
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle_shape(length, width):
    """
    5. Function with more than one inputs and/or outputs
    This function demonstrates how a function returns multiple outputs
    This function calculates the area and perimeter of a rectangle
    length: the length of a square, must be a positive number
    width: the width of a square, must be a positive number
    area  : the area of the square, must be a positive number
    perimeter: the perimeter of the square, must be a positive number
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def square_default(side=5):
    """
    6. Function with a default input parameter and more than one outputs
    This function demonstrates how a function handles a default input argument
    This function calculates the area and perimeter of a square
    side: the side of the square; if not provided, the side will be set to 5
    area  : the area of the square, must be a positive number
    perimeter: the perimeter of the square, must be a positive number
    """
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle_default(length=7, width=4):
    """
    7. Function with more than one default input arguments
    This function demonstrates how a function handles more than one input 
    arguments and returns multiple outputs
    This function calculates the area and perimeter of a rectangle
    length: the length of a rectangle, default value is set to 7
    width: the width of a rectangle, default value is set to 4
    area  : the area of the square, must be a positive number
    perimeter: the perimeter of the square, must be a positive number
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

if __name__ == "__main__":
    # blank_function()
    area_square_01, peri_square_01 = square_default()    
    print(area_square_01)
    print(peri_square_01)

    # 8. Anonymous Function (lambda notation in C++ / closure in Swift)
    # Unlike the previous functions that must be begun with def,
    # lambda notation inlcudes lambda keyword inside the function declaration
    # This method allows a more concise function implementation
    area_rect_lambda = lambda w, l: (w*l)
    peri_rect_lambda = lambda w, l: 2*(w+l)
    # Calling anonymous function
    print( area_rect_lambda(10, 5) )
    print( peri_rect_lambda(10, 5) )






