class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        while self.stack and self.stack[-1][0] <= price:
            result += self.stack.pop()[1]

        self.stack.append((price, result))
        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


class TestStockSpanner:
    def test_example1(self):
        stockSpanner = StockSpanner()
        assert stockSpanner.next(100) == 1
        assert stockSpanner.next(80) == 1
        assert stockSpanner.next(60) == 1
        assert stockSpanner.next(70) == 2
        assert stockSpanner.next(60) == 1
        assert stockSpanner.next(75) == 4
        assert stockSpanner.next(85) == 6
