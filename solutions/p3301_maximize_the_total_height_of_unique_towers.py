# Title: Maximize the Total Height of Unique Towers
# Link: https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/
# Difficulty: Medium

from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        currentHeight = maximumHeight[0]
        sum = 0
        for height in maximumHeight:
            currentHeight = min(currentHeight, height)
            if currentHeight <= 0:
                return -1
            sum += currentHeight
            currentHeight -= 1
        return sum


class TestMaximumTotalSum:
    def test_example1(self):
        maximumHeight = [2, 3, 4, 3]
        assert Solution().maximumTotalSum(maximumHeight) == 10

    def test_example2(self):
        maximumHeight = [15, 10]
        assert Solution().maximumTotalSum(maximumHeight) == 25

    def test_example3(self):
        maximumHeight = [2, 2, 1]
        assert Solution().maximumTotalSum(maximumHeight) == -1
