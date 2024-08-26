import random
from hangman_words import word_list


# Create a class for the chosen word

class HangmanWord:
    def __init__(self):
        self.answer = random.choice(word_list)
        self.length = len(self.answer)
