# Title: Best Time to Buy and Sell Stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


class TestMaxProfit:
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        assert Solution().maxProfit(prices) == 5

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        assert Solution().maxProfit(prices) == 0

    def test_example3(self):
        prices = [2, 4, 1]
        assert Solution().maxProfit(prices) == 2
