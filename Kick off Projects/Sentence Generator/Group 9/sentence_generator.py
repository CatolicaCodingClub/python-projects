#Sentence generator game

import random

a = ["My", "Your", "His", "Her", "Our", "Their", "The", "A"]
b = ["car", "hair", "boat", "house", "food", "smartphone", "jacket", "shirt", "computer"]
c = ["is", "was", "looks"]
d = ["nice", "cheap", "expensive", "good", "clean", "dirty", "new", "old", "big", "small"]

FirstWord = random.choice(a)
SecondWord = random.choice(b)
ThirdWord = random.choice(c)
ForthWord = random.choice(d)

sentence = FirstWord + " " + SecondWord + " " + ThirdWord + " " + ForthWord + "."
print(sentence)
