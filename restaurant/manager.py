from restaurant.disklogger import DiskLogger
from time import time,localtime
from pprint import pprint

class Manager(DiskLogger):

    def __init__(self, cash_desk, kitchen, give_away):
        super().__init__('Manager')
        self.cash_desk = cash_desk
        self.kitchen = kitchen
        self.give_away = give_away

    def new_order(self, order):
        order.road_taken.append(f'MG {time()}')
        order.log('Manager NO')
        self.logd(f'{order.name} Manager NO')
        self.kitchen.prepare_meal(order)

    def meal_ready(self, order):
        order.road_taken.append(f'MN {time()}')
        self.logd(f'{order.name} Manager MR')
        self.call_customer(order)

    def call_customer(self, order):
        order.road_taken.append(f'MN CCall {time()}')
        self.logd(f'{order.name} Manager CCall')
        self.customer_collected_order(order)


    def customer_collected_order(self, order):
        order.road_taken.append(f'Customer {time()}')
        order.time_given_away=time()
        print(f'Order complete: {order.name} Ordered: {order.time_ordered} '
              f'Finished: {order.time_finished} Given: {order.time_given_away}')
        print(f'  Road taken: ')
        pprint(order.road_taken)
        print(order)