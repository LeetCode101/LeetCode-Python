class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        price_span = 1

        while self.prices and self.prices[-1][0] <= price:
            _, prev_span = self.prices.pop()
            price_span += prev_span

        self.prices.append((price, price_span))

        return price_span
