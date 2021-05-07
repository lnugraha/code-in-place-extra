import random

def main():
    # Check if there questions have been answered consecutively
    counter = 0
    while True:
        if counter != 3:
            numOne = random.randint(0, 10)
            numTwo = random.randint(0, 10)
            print("What is the addition of {} and {}".format(numOne, numTwo))
            answer = input("Your answer is ")
            answer = int(answer)
            if answer == (numOne + numTwo):
                counter = counter + 1
                print("Correct answer! You have answered {} questions correctly".format(counter))
            else:
                counter = 0
                print("Wrong answer, the game is reset")
        else:
            print("The game ends here since you have answered 3 questions correctly")
            break
if __name__ == "__main__":
    main()
