import random
from hangman_art import stages, logo
from hangman_words import word_list

# TODO 1: Choose a word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# TODO 2: Game
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks to display and replace with letters chosen by the user
display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()

    # TODO 3: If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed '{guess}'. Please try another letter.")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO 4: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Your chosen guess, '{guess}', is not in the word.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(stages[lives])
            break
        print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        print("You win.")
