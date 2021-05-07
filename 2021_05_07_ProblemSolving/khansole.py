import random

def main():
    numOne = random.randint(0, 10)
    numTwo = random.randint(0, 10)
    print("What is the addition of " + str(numOne) + " + " + str(numTwo))
    answer = input("Please enter your answer: ")
    answer = int(answer)
    if answer != (numOne + numTwo):
        print("Incorrect, the answer should be " + str(numOne+numTwo))
    else:
        print("Correct answer")

if __name__ == "__main__":
    main()
