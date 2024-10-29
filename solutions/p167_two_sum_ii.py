# Title: Two Sum II - Input array is sorted
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n) solution
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []


class TestTwoSum:
    def test_example1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        assert Solution().twoSum(numbers, target) == expected

    def test_example2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        assert Solution().twoSum(numbers, target) == expected

    def test_example3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        assert Solution().twoSum(numbers, target) == expected
