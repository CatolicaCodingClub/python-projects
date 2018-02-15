#Roll the dice game

import random
from tkinter import messagebox

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)

print("1st dice:", a)
print("2nd dice:",b)
print("3rd dice:", c)

if a == b == c:
    print("Yatzy!")
    messagebox.showinfo("All three dices are the same","Yatzy!")
else:
    print("Too bad. Try again!")
