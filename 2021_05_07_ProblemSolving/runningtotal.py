import math

def running_total():
    
    inputInt = input("Enter your first number: ")
    inputInt = int(inputInt)
    
    if inputInt != 0:
        sumTotal = inputInt
        
        while True:
            nextInt = input("Enter an integer: ")
            nextInt = int(nextInt)
            sumTotal = sumTotal + nextInt
            
            if nextInt == 0:
                print("The cumulative sum: {}".format(sumTotal))
                break
            else:
                print("The current cumulative sum: {}".format(sumTotal))
                continue

    else:
        print("Your input number is zero, so the program terminates")

if __name__ == "__main__":
    running_total()



