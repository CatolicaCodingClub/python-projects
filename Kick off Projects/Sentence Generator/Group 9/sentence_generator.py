#Sentence generator game

import random

a = random.randint(0,7)
b = random.randint(0,8)
c = random.randint(0,2)
d = random.randint(0,9)

FirstWord = ["My", "Your", "His", "Her", "Our", "Their", "The", "A"]
SecondWord = ["car", "hair", "boat", "house", "food", "smartphone", "jacket", "shirt", "computer"]
ThirdWord = ["is", "was", "looks"]
ForthWord = ["nice", "cheap", "expensive", "good", "clean", "dirty", "new", "old", "big", "small"]

sentence = FirstWord[a]+ " " + SecondWord[b] + " " + ThirdWord[c] + " " + ForthWord[d] + "."
print(sentence)