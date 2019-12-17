from random import randint

BOARD_SIZE = 10
DICE_SIZE = 6
INITIAL_BALANCE = 300
BALANCE_ROUND_INCREASE = 100


class Player:
    def __init__(self):
        self.balance = INITIAL_BALANCE
        self.position = 0

    def move(self):
        dice_result = randint(1, DICE_SIZE)
        self.position += dice_result
        if self.position >= BOARD_SIZE:
            self.position %= BOARD_SIZE
            self.balance += BALANCE_ROUND_INCREASE

    def want_buy(self, property_):
        raise NotImplementedError

    def buy(self, property_):
        self.balance -= property_.value
        property_.owner = self

    def pay_rent(self, property_):
        property_.owner.balance += property_.rent
        self.balance -= property_.rent

    def do_buy_action(self, property_):
        if property_.owner:
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
