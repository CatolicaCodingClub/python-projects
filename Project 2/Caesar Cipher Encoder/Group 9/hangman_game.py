# hangman game

import random
import re

#Alternatively to creating the list with words in the script, you can also import a list from excel
"""
import pandas as pd
data = pd.read_csv("/username/folder/hangman_game.csv")
word_list = data.iloc[:, 0]
"""

word_list = ["Germany", "eat", "horse", "football", "food", "drink", "space", "Australia", "university"]

word = random.choice(word_list).lower()
answer = list("_" * len(word))
print("The word has " + str(len(word)) + " letters")
print(answer)
print()
s = 0

while s < 11:
    letter = input("Input a letter or word: ").lower()

    if len(letter) == 1:

        if word.count(letter) == 1:
            letter_ind = word.index(letter)
            answer[letter_ind] = letter
        elif word.count(letter) > 1:
            letter_ind = [m.start() for m in re.finditer(letter, word)]
            replace_letter = [letter] * len(letter_ind)

            for x,y in zip(letter_ind, replace_letter):
                    answer[x] = y

        else:
            print("The word does not include this letter")

    else:
        if word == letter:
            answer = list(letter)
            break
        else:
            print("The word you guessed is incorrect")

    if answer.count("_") == 0:
        break

    print(answer)
    s = s + 1

    if int(11 - s) > 1:
        print("You have " + str(11 - s) + " tries left")
    elif int(11 - s) == 1:
        print("You have 1 more try left")
    else:
        print("You have no more tries left")

    print()

print()
if answer.count("_") == 0:
    print("You did it! The correct word is " + "".join(answer))
else:
    print("You failed! Try again")