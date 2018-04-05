"""
20 random cards are placed in a row, all face down. A move consists of turning a face down card face up and turning
over the card immediately to the right. Show that no matter what the choice of cards to turn, this sequence of
moves must terminate.
"""
import numpy as np

face_down = 1
face_up = 0

rand_card = np.random.randint(0, 20)
cards = []
nr_moves = 0

for x in range(20):
    cards.append(face_down)

print(cards)

while cards.count(face_down) != 0:

    if rand_card != 19:

        if cards[rand_card] == face_down:
            cards[rand_card] = face_up

            if cards[rand_card + 1] == face_down:
                cards[rand_card + 1] = face_up
            else:
                cards[rand_card + 1] = face_down

            nr_moves = nr_moves + 1
            print(cards)

        elif cards.count(face_down) == 0:
            break
        else:
            rand_card = np.random.randint(0, 20)

    else:
        rand_card = np.random.randint(0, 20)

print("This sequence of moves terminates after " + str(nr_moves) + " moves.")