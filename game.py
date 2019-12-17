from entities import player, property

TIME_OUT_ROUNDS = 5

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
        self.round = 0

    def run(self):
        while self.round <= TIME_OUT_ROUNDS:
            for p in self.players:
                p.move()
                print(f'{p} - {self.properties[p.position]}')
                p.do_buy_action(self.properties[p.position])
                print(f'{p} - {p.balance}')

            self.round += 1


if __name__ == '__main__':
    g = Game()
    g.run()
