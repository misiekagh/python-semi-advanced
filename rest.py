from restaurant.manager import Manager
from restaurant.cash_desk import CashDesk
from restaurant.give_away import GiveAway
from restaurant.kitchen import Kitchen
from restaurant.order import Order

if __name__=='__main__':
    cashdesk = CashDesk(None)
    giveaway = GiveAway(None)
    kitchen = Kitchen(None)

    manager = Manager(cashdesk, kitchen, giveaway)

    cashdesk.manager = manager
    giveaway.manager = manager
    kitchen.manager = manager

    cashdesk.new_order(Order('Burger'))
    cashdesk.new_order(Order('Pizza'))
