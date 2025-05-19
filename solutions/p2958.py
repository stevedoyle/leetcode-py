# 2958. Length of Longest Subarray With at Most K Frequency
# URL: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# Difficulty: Medium

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqs = defaultdict(int)
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            freqs[num] += 1

            while freqs[num] > k:
                freqs[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


class TestMaxSubarrayLength:
    def test_example1(self):
        nums = [1, 2, 3, 1, 2, 3, 1, 2]
        k = 2
        expected = 6
        s = Solution()
        result = s.maxSubarrayLength(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 1, 2, 1, 2, 1, 2]
        k = 1
        expected = 2
        s = Solution()
        result = s.maxSubarrayLength(nums, k)
        assert result == expected

    def test_example3(self):
        nums = [5, 5, 5, 5, 5, 5, 5]
        k = 4
        expected = 4
        s = Solution()
        result = s.maxSubarrayLength(nums, k)
        assert result == expected
