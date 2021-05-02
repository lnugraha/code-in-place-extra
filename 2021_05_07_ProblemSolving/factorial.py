import math

def factorial_for(n):
    result = 1
    for i in range(1, n+1, 1):
        result = result * i
    return result

def factorial_recursive(n):
    if (n == 1 or n == 0):
        return 1 # Base Case
    elif (n > 1):
        return factorial_recursive(n-1)*n

if __name__ == "__main__":
    check = factorial_for(5)
    print(check)

    test = factorial_recursive(5)
    print(test)
