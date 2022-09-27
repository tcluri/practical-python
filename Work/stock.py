class Stock:
    def __init__(self, stockname, shares, price):
        self.name = stockname
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, num_shares):
        self.shares -= num_shares
    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
