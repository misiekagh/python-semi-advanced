from dataclasses import dataclass

@dataclass

@dataclass
class Player:
    name: str
    ranking: int

    def __post_init__(self):
        try: assert(len(self.name)>3)
        except: print('Nazwa Playera za krótka')

    def description(self):
        return f'My name is {self.name} and my ranking is {self.ranking}.'

@dataclass
class Arena:
    games = []
    standing = [Player('Jan Lewandowski', 1200)]

    def __post_init__(self):
        print('Adding arena')

    def add_game(self, game):
        self.games.append(game)
        return game


@dataclass
class Game:
    white: Player
    black: Player
    winner: int

    def whiteWon(self):
        return True

    def blackWon(self):
        return True

