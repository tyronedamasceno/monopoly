from random import randint

from game import BOARD_SIZE, BALANCE_ROUND_INCREASE, INITIAL_BALANCE, DICE_SIZE


class Player:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.position = 0

    def move(self):
        dice_result = randint(1, DICE_SIZE)
        print(f'{self} moving {dice_result} from {self.position}', end=' ')
        self.position += dice_result
        if self.position >= BOARD_SIZE:
            self.position %= BOARD_SIZE
            self.balance += BALANCE_ROUND_INCREASE
        print(f'to {self.position}')

    def want_buy(self, property_):
        raise NotImplementedError

    def buy(self, property_):
        print(f'{self} buys {property_}')
        self.balance -= property_.value
        property_.owner = self

    def pay_rent(self, property_):
        print(f'{self} pays {property_.rent} of rent to {property_.owner}')
        property_.owner.balance += property_.rent
        self.balance -= property_.rent

    def do_buy_action(self, property_):
        print(f'{self} doing buy action')
        if property_.owner:
            print(f'but {property_} is already owned')
            self.pay_rent(property_)
            return

        if self.balance >= property_.value and self.want_buy(property_):
            self.buy(property_)

    def __repr__(self):
        return f'{self.behavior.capitalize()}Player'


class ImpulsivePlayer(Player):
    behavior = 'impulsive'

    def want_buy(self, property_):
        return True


class RigorousPlayer(Player):
    behavior = 'rigorous'

    def want_buy(self, property_):
        return property_.rent > 50


class PrudentPlayer(Player):
    behavior = 'prudent'

    def want_buy(self, property_):
        return self.balance - property_.value >= 80


class RandomicPlayer(Player):
    behavior = 'randomic'

    def want_buy(self, property_):
        return bool(randint(0, 1))
