# Title: 1829. Maximum XOR for Each Query
# URL: https://leetcode.com/problems/maximum-xor-for-each-query/
# Difficulty: Medium

from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        max_xor = (1 << maximumBit) - 1
        result = []
        for i in range(n):
            result.append(max_xor ^ xor_sum)
            xor_sum ^= nums[n - i - 1]
        return result


class TestGetMaxXor:
    def test_example1(self):
        nums = [0, 1, 1, 3]
        maximumBit = 2
        assert Solution().getMaximumXor(nums, maximumBit) == [0, 3, 2, 3]

    def test_example2(self):
        nums = [2, 3, 4, 7]
        maximumBit = 3
        assert Solution().getMaximumXor(nums, maximumBit) == [5, 2, 6, 5]

    def test_example3(self):
        nums = [0, 1, 2, 2, 5, 7]
        maximumBit = 3
        assert Solution().getMaximumXor(nums, maximumBit) == [4, 3, 6, 4, 6, 7]
