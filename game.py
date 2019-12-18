from entities import player, property

TIME_OUT_ROUNDS = 500
BOARD_SIZE = 10
DICE_SIZE = 6
INITIAL_BALANCE = 300
BALANCE_ROUND_INCREASE = 100

property_instances = [
    {'name': 'Copacabana', 'value': 150, 'rent': 45},
    {'name': 'Morumbi', 'value': 120, 'rent': 30},
    {'name': 'Faria Lima', 'value': 160, 'rent': 60},
    {'name': 'Interlagos', 'value': 100, 'rent': 35},
    {'name': 'Leblon', 'value': 135, 'rent': 55},
    {'name': 'Av. Paulista', 'value': 180, 'rent': 70},
    {'name': 'Flamengo', 'value': 95, 'rent': 35},
    {'name': 'Botafogo', 'value': 115, 'rent': 40},
    {'name': 'Luz', 'value': 75, 'rent': 15},
    {'name': 'Lapa', 'value': 80, 'rent': 25},
]


class Game:
    def __init__(self):
        self.players = [
            player.ImpulsivePlayer(), player.RigorousPlayer(),
            player.PrudentPlayer(), player.RandomicPlayer()
        ]
        self.properties = [
            property.Property(**property_instance)
            for property_instance in property_instances
        ]
        self.round = 1

    def run(self):
        while self.round <= TIME_OUT_ROUNDS and len(self.players) > 1:
            print(f'\n#{self.round} round beginning', end='\n\n')
            for p in self.players:
                p.move()
                p.do_buy_action(self.properties[p.position])
                if p.balance < 0:
                    self.remove_player_from_game(p)
            self.show_partial_results()
            self.round += 1
        self.show_final_result()

    def remove_player_from_game(self, player_):
        print(f'{player_} lost the game and lose all his properties')
        for property_ in self.properties:
            if property_.owner == player_:
                property_.owner = None
        self.players = [p for p in self.players if p != player_]

    def show_partial_results(self):
        print('\nShow partial results\n')
        for p in self.players:
            print(f'{p} is at {p.position} with {p.balance} of balance')
            player_properties = ', '.join([
                property_.name
                for property_ in self.properties if property_.owner == p
            ])
            if player_properties:
                print(f'{p} has following properties: {player_properties}')
            else:
                print(f'{p} has no properties yet')

    def show_final_result(self):
        pass


if __name__ == '__main__':
    g = Game()
    g.run()
