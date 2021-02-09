class Contract:
    def __init__(self, name, buy_price, sell_price):
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price

    def __repr__(self):
        return self.name + " at " + self.sell_price