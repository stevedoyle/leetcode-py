# Title: Best Time to Buy and Sell Stock II
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Difficulty: Medium

from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i - 1], 0)
        return max_profit


class TestMaxProfit:
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        s = Solution()
        result = s.maxProfit(prices)
        assert result == expected

    def test_example2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        s = Solution()
        result = s.maxProfit(prices)
        assert result == expected

    def test_example3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        s = Solution()
        result = s.maxProfit(prices)
        assert result == expected
