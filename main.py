from hangman_art import logo
from word_model import HangmanWord
from player_model import HangmanPlayer
from game_brain import GameBrain

hangman_word = HangmanWord()
players = []

print(logo)

num_players = int(input("How many players? "))
# Testing code
# print(f'Pssst, the solution is {hangman_word.answer}.')

for player_num in range(num_players):
    player_name = input(f"What is player #{player_num}'s name: ")
    players.append(HangmanPlayer(player_name, hangman_word))

hangman_game = GameBrain(players)

while not hangman_game.is_game_over():
    hangman_game.run_game(hangman_word)

print(f"Congrats to {hangman_game.winner.name}!")
print(f"Better luck next time to our remaining players:\n{hangman_game.losers}")
