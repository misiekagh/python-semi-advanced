from dataclasses import dataclass
from time import time, localtime

@dataclass
class Order:
    name: str
    time_ordered = time()
    time_finished = 0.0
    time_given_away = 0.0
    road_taken = []

    def __str__(self):
        return f'Order {self.name} {localtime(self.time_ordered)}'

    def log(self, loc):
        print(f'{self.name} {time()} im currently in {loc}' )
