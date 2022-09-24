from random import randint, random
numberOfTries = 3
while True:
    data = int(input("Enter a number "))
    numberOfTries -= 1
    if randint(1, 10) == data:
        print("congratulation,Correct number ")
        break
    else:
        if numberOfTries == 0:
            print("sorry ,your tries failed ")
            break
        numberOfTries -= 1
        data = int(input("Enter a number "))
