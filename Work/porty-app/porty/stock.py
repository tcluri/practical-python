from . import typedproperty as tp


class Stock:
    name = tp.String('name')
    shares = tp.Integer('shares')
    price = tp.Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

    # @property
    # def shares(self):
    #     return self._shares

    # @shares.setter
    # def shares(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError('expected an integer')
    #     self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares):
        self.shares -= num_shares
