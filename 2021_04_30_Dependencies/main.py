"""
April 27, 2021
This program provides an example on how to utilize Python built-in library
This program aims to take a square root of an integer and return the result
Notice that I designed two functions that accomplish the exact same purpose:
    version_01: using import math           (access all functions inside math)
    version_02: using from math import sqrt (only access sqrt function)
"""

def square_root_version_01(num):
    import math
    if num < 0:
        # This is an exception handler in a simple way
        print("ERROR: This function only accepts postive integer")
        return None
    elif type(num) is not int:
        print("ERROR: The input number is not an integer")
        return None
    return math.sqrt(num) # Check this part!

def square_root_version_02(num):
    from math import sqrt
    if num < 0:
        # This is an exception handler in a simple way
        print("ERROR: This function only accepts postive integer")
        return None
    elif type(num) is not int:
        print("ERROR: The input number is not an integer")
        return None
    return sqrt(num) # Check this part


if __name__ == "__main__":
    check_01 = square_root_version_02(25)
    print(check_01)

    # This case causes an error
    check_02 = square_root_version_01(-36)

    # This case causes another error since we need an integer
    check_03 = square_root_version_01(25.00)
