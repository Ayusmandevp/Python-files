import random
target=random.randint(1,100)

while True:
    userChoice=int(input("Guess the target between 1 to 100:"))
    if (userChoice==target):
        print("You have guessed Successfully...")
        break
    elif (userChoice<target):
        print("You have chosen a smaller number than target choose again...")
    else:
        print("You have chosen a larger number than target choose again...")
