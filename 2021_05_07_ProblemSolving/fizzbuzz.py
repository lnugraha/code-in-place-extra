import math

fizz = 5; buzz = 3

def fizzbuzz_forloop():
    n = 31
    for i in range(1, n, 1):
        if (i % (fizz * buzz) == 0):
            print("FizzBuzz {}".format(i))
        elif (i % fizz == 0):
            print("Buzz {}".format(i))
        elif (i % buzz == 0):
            print("Fizz {}".format(i))
        else:
            print(i)

def fizzbuzz_while():
    n = 31; i = 0
    while i < n:
        if (i % (fizz * buzz) == 0):
            print("FizzBuzz {}".format(i))
        elif (i % fizz == 0):
            print("Buzz {}".format(i))
        elif (i % buzz == 0):
            print("Fizz {}".format(i))
        else:
            print(i)
        i = i+1

if __name__ == "__main__":
    fizzbuzz_forloop()
    fizzbuzz_while()
