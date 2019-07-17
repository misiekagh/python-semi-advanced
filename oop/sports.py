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

    ''' stworz liste zawodnikow 2. stworz mape liczba zwycies
    3. posortuj'''
    def standing1(self, playes):
        result = []
        players = []
        for game in self.games:
            if game.white not in players:
                players.append(game.white)
                scores.append(0)
            if game.black not in players:
                players.append(game.black)
                scores.append(0)
            if game.white_won():
                index=players.index(game.white)
            else:
                index = players.index(black)
            scores[index]+=1
        player_score_list=list(zip(players, scores))
        player_score_list.sort(key=lambda x: x[1], reverse=True)
        return [pair[0] ]

@dataclass
class Game:
    white: Player
    black: Player
    winner: int

    def whiteWon(self):
        return True

    def blackWon(self):
        return True

