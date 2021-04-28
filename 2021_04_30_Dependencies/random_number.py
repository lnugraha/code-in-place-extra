"""
April 28, 2021
By Leo Nugraha
This program demonstrates the following topics:
    1. How to generate random number
    2. How to use Python built-in library dependency 
"""

def random_1_to_8_ver_01():
    import random
    random_number = random.randint(1,8)
    return random_number

def random_1_to_8_ver_02():
    import random
    # Multiply it by seven to have a range between 0 and 7, 
    # then add one to shift the range from 1 to 8
    random_number = int( random.random()*7 ) + 1
    return random_number

if __name__ == "__main__":
    test_01 = random_1_to_8_ver_01()
    print("The first random number: {}".format(test_01))
    test_02 = random_1_to_8_ver_02()
    print("The second random number: {}".format(test_02))
