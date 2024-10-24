# Title: Container With Most Water
# URL: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


class TestMaxArea:
    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        assert Solution().maxArea(height) == 49

    def test_example2(self):
        height = [1, 1]
        assert Solution().maxArea(height) == 1
