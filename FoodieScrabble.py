
# First basic structure, def needs adjustments :)


import random


class ScrabbleGame:
    def __init__(self):
        self.dictionary = set(["apple", "banana", "cherry"])  # Predefined word dictionary
        self.players = ["Player 1", "Player 2"] #need to add  more players
        self.scores = {player: 0 for player in self.players}
        self.tiles = list("abcdefghijklmnopqrstuvwxyz")  # A-Z as tiles (use a more realistic tile distribution)

    def draw_tiles(self, count):
        return random.sample(self.tiles, count)

    def is_valid_word(self, word):
        return word.lower() in self.dictionary

    def calculate_score(self, word):
        # Simplified scoring: 1 point per letter
        return len(word)


def main():
    game = ScrabbleGame()

    while True:
        for player in game.players:
            print(f"{player}'s turn:")
            tiles = game.draw_tiles(7)
            print("Your tiles:", ' '.join(tiles))

            word = input("Enter a word: ").strip()

            if not word:
                print("Goodbye!")
                return

            if game.is_valid_word(word):
                score = game.calculate_score(word)
                game.scores[player] += score
                print(f"Valid word! You scored {score} points.")
            else:
                print("Not a valid word.")

            print("Current scores:")
            for p, score in game.scores.items():
                print(f"{p}: {score}")
            print()


if __name__ == "__main__":
    main()
