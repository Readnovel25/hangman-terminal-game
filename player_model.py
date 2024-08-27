from hangman_art import stages

HANGMAN_LIVES = 6


class HangmanPlayer:
    def __init__(self, name, word):
        self.name = name
        self.lives = HANGMAN_LIVES
        self.stage = stages[HANGMAN_LIVES]
        self.display = ["_" for _ in range(word.length)]
        self.is_loser = False
        self.is_winner = False

    def show_display(self):
        print(f"{' '.join(self.display)}")

    def update_display(self, guess, word):
        if guess in self.display:
            print(f"You have already guessed '{guess}'. Please try another letter next time.")
        for position in range(word.length):
            letter = word.answer[position]
            if letter == guess:
                self.display[position] = letter

    def update_stages_lives(self, guess, word):
        if guess not in word.answer:
            print(f"Your chosen guess, '{guess}', is not in the word.")
            self.lives -= 1
            self.stage = stages[self.lives]
            print(self.stage)

    def has_won(self, lives):
        if "_" not in self.display:
            self.is_winner = True
            print(f"You win, {self.name}")
        if lives == 0:
            print(f"You lose, {self.name}. Better luck next time!")
            self.is_loser = True
