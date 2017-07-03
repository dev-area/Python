
import showcard
import random

showcard.set_timeout(1)

cards = list(range(1,52))
random.shuffle(cards)

try:
    for card in cards:
        filename = 'BMP' + str(card) + '.gif'
        showcard.display_file(filename)
except KeyboardInterrupt:
    exit('Bye...')