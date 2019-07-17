from time import time
from restaurant.disklogger import DiskLogger

class Kitchen(DiskLogger):
    def __init__(self, manager):
        super().__init__('Kitchen')
        self.manager = manager

    def prepare_meal(self, order):
        order.road_taken.append(f'KT {time()}')
        order.log('Kitchen PM')
        self.logd(f'{order.name} Kitchen PM')
        self.meal_ready(order)

    def meal_ready(self, order):
        order.time_finished=time()
        order.log('Kitchen RDY')
        self.logd(f'{order.name} Kitchen RDY')
        self.manager.meal_ready(order)
