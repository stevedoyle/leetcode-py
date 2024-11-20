# Title: Maximum Sum of Distinct Subarrays with Length K
# URL: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Difficulty: Medium

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        max_sum = 0
        curr_sum = 0
        begin = 0
        end = 0
        num_to_idx = {}

        while end < len(nums):
            curr_num = nums[end]
            last_occurrence = num_to_idx.get(curr_num, -1)

            while begin <= last_occurrence or end - begin + 1 > k:
                curr_sum -= nums[begin]
                begin += 1
            num_to_idx[curr_num] = end
            curr_sum += curr_num

            if end - begin + 1 == k:
                max_sum = max(max_sum, curr_sum)

            end += 1

        return max_sum


class TestMaxSubarraySum:
    def test_example1(self):
        nums = [1, 5, 4, 2, 9, 9, 9]
        k = 3
        expected = 15
        assert Solution().maximumSubarraySum(nums, k) == expected

    def test_example2(self):
        nums = [4, 4, 4]
        k = 3
        expected = 0
        assert Solution().maximumSubarraySum(nums, k) == expected

    def test_example3(self):
        nums = [9, 9, 9, 1, 2, 3]
        k = 3
        expected = 12
        assert Solution().maximumSubarraySum(nums, k) == expected
