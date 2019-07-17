from dataclasses import dataclass
from time import time
from restaurant.disklogger import DiskLogger

@dataclass
class CashDesk(DiskLogger):
    manager = None

    def new_order(self, order):
        order.road_taken=[]
        order.road_taken.append(f'CD {time()}')
        order.log('CashDesk')
        self.logname='CashDesk'
        self.logd(f'{order.name} CashDesk NO')
        self.manager.new_order(order)
