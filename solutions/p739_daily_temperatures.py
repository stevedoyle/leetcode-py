# Title: Daily Temperatures
# URL: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result


class TestDailyTemperatures:
    def test_example1(self):
        assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
            1,
            1,
            4,
            2,
            1,
            1,
            0,
            0,
        ]

    def test_example2(self):
        assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    def test_example3(self):
        assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
