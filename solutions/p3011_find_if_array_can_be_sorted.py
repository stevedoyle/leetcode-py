# Title: Find if Array Can Be Sorted
# URL: https://leetcode.com/problems/find-if-array-can-be-sorted/
# Difficulty: Medium

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        values = nums.copy()

        for i in range(n):
            for j in range(n - 1 - i):
                if values[j] <= values[j + 1]:
                    continue
                else:
                    if values[j].bit_count() == values[j + 1].bit_count():
                        values[j], values[j + 1] = values[j + 1], values[j]
                    else:
                        return False
        return True


class TestCanSortArray:
    def test_example1(self):
        nums = [8, 4, 2, 30, 15]
        assert Solution().canSortArray(nums)

    def test_example2(self):
        nums = [1, 2, 3, 4, 5]
        assert Solution().canSortArray(nums)

    def test_example3(self):
        nums = [3, 16, 8, 4, 2]
        assert not Solution().canSortArray(nums)
