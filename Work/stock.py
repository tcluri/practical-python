class Stock:
    def __init__(self, stockname, shares, price):
        self.name = stockname
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected an integer')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price
    def sell(self, num_shares):
        self.shares -= num_shares
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
