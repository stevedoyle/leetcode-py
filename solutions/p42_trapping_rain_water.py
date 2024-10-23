# Title: Trapping Rain Water
# URL: https://leetcode.com/problems/trapping-rain-water/
# Difficulty: Hard

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        ans = 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


class TestTrap:
    def test_example1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        assert Solution().trap(height) == expected

    def test_example2(self):
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        assert Solution().trap(height) == expected
