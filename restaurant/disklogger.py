from dataclasses import dataclass
from time import time

@dataclass
class DiskLogger:
    logname: str

    def logd(self, msg):
        try:
            with open(self.logname + '.log', 'a', encoding='utf8') as file:
                file.write(f'[{time()}] {msg}\n')
        except:
            print(f'{self.logname} Can\'t write to log')
