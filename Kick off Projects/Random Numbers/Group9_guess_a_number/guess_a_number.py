#Guess a number game
# x is the variable of the number that has to be guessed
# y is the variable for the number that you pick
# s is the variable that counts your tries

import random
x = random.randint(1,20)
s = 0

while s < 5:
    y = int(input("Guess a number between 1 and 20:"))
    if y == x:
        print("Congratulations, you guessed right!")
        break
    if y > x:\
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")
    s = s + 1
    print("You have " + str(5-s) + " tries left")
