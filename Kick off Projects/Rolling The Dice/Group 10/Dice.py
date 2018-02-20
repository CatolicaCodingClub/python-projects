import random

a1 = random.randint(1, 6)
b1 = random.randint(1, 6)
c1 = random.randint(1, 6)


a2 = random.randint(1, 6)
b2 = random.randint(1, 6)
c2 = random.randint(1, 6)

print("Rules:")
print("The player with higher sum of dices' numbers wins.")
print("If one player gets all dices with the same number he automatically wins!")
print("")
print("Player 1")
print(a1)
print(b1)
print(c1)
if a1==b1==c1 :
    print("Yatzy!")

print("")

print("Player 2")
print(a2)
print(b2)
print(c2)
if a2==b2==c2 :
    print("Yatzy!")
print("")

if a1==b1==c1 and a2==b2==c2 :
    print("Draw!")
elif a1==b1==c1 :
    print("Player 1 Wins!")
elif a2==b2==c2 :
    print("Player 2 Wins")
else :
    Sum1 = a1+b1+c1
    Sum2 = a2+b2+c2
    print("Player 1:", Sum1)
    print("Player 2:", Sum2)
    print("")
    if Sum1 > Sum2 :
        print ("Player 1 Wins!")
    elif Sum1 < Sum2 :
        print("Player 2 Wins!")
    elif Sum1 == Sum2 :
        print("Draw!")
