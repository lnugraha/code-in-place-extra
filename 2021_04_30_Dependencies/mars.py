"""
April 28, 2021
By Leo Nugraha
This program demonstrates how a simple function is written in Python
The function handles an input and generates an output
"""
import math

def weight_in_mars(earth_weight):
    # Assume the earth_weight is stored as a decimal, but not integer
    MARS_GRAVITY = 0.378
    # The following checks if the input is correct
    # What if the input is non-number
    if (type(earth_weight) != float):
        print("ERROR: Weight data type in not a number")
        return None
    # What if the input is negative?
    if (earth_weight < 0.0):
        print("ERROR: Weight must be positive number")
        return None
    # Proceed to calculate the result
    mars_weight = MARS_GRAVITY * earth_weight
    # Return your result
    return mars_weight

if __name__ == "__main__":
    # Case 1: Everything is fine
    test_01 = weight_in_mars(100.00)
    print(test_01)
    # Case 2: Negative weight
    test_02 = weight_in_mars(-100.0)
    # Case 3: String input
    test_03 = weight_in_mars("100")
