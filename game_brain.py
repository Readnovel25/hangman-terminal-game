# This game brain should be able to detect when a game is over
# AKA when a player has guessed the word or when all players have lost
# It should also remove players from the active player list once they have lost

class GameBrain:
    def __init__(self, players):
        self.winner = None
        self.active_players = players
        self.losers = []
        self.game_won = False

    def is_game_over(self):
        if len(self.active_players) == 0 or self.game_won:
            return True
        return False

    def remove_player(self, player):
        player_index = self.active_players.index(player)
        if player.is_loser:
            loser_player = self.active_players.pop(player_index)
            self.losers.append(loser_player.name)

    def run_game(self, word):
        for player in self.active_players:
            player.show_display()
            player.guess = input(f"{player.name}, guess a letter: ").lower()
            player.update_display(player.guess, word)
            player.update_stages_lives(player.guess, word)
            player.has_won(player.lives)
            self.remove_player(player)
            if player.is_winner:
                self.winner = player
                self.game_won = True
                break
            player.show_display()
