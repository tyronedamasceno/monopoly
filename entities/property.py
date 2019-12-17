class Property:
    def __init__(self, name, value, rent):
        self.name = name
        self.value = value
        self.rent = rent
        self.owner = None

    def __repr__(self):
        return f'Property({self.name}, {self.value}, {self.rent})'
