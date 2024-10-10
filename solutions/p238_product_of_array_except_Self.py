# Title: 238. Product of Array Except Self
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        left = 1
        right = 1
        for i in range(n):
            output[i] *= left
            output[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
        return output

    def productExceptSelfv2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        # output[i] contains the product of all the elements to the left
        # Note: output[0] is 1 because there are no elements to the left
        # of the first element
        output[0] = 1
        for i in range(1, n):
            # output[i] contains the product of all the elements to the left
            # of nums[i]
            output[i] = output[i - 1] * nums[i - 1]

        # right contains the product of all the elements to the right
        right = 1
        for i in reversed(range(n)):
            output[i] *= right
            right *= nums[i]
        return output


class TestProductExceptSelf:
    def test_example1(self):
        input = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        assert Solution().productExceptSelf(input) == output
        assert Solution().productExceptSelfv2(input) == output

    def test_example2(self):
        input = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        assert Solution().productExceptSelf(input) == output
        assert Solution().productExceptSelfv2(input) == output
