# Title: Shortest Subarray to be Removed to Make Array Sorted
# URL: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# Difficulty: Medium

from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1
        return ans


class TestShortestSubarray:
    def test_example1(self):
        arr = [1, 2, 3, 10, 4, 2, 3, 5]
        expected = 3
        assert Solution().findLengthOfShortestSubarray(arr) == expected

    def test_example2(self):
        arr = [5, 4, 3, 2, 1]
        expected = 4
        assert Solution().findLengthOfShortestSubarray(arr) == expected

    def test_example3(self):
        arr = [1, 2, 3]
        expected = 0
        assert Solution().findLengthOfShortestSubarray(arr) == expected
