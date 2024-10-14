# Title: 135. Candy
# URL: https://leetcode.com/problems/candy/
# Difficulty: Hard

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


class TestCandy:
    def test_example1(self):
        ratings = [1, 0, 2]
        expected = 5
        assert Solution().candy(ratings) == expected

    def test_example2(self):
        ratings = [1, 2, 2]
        expected = 4
        assert Solution().candy(ratings) == expected
