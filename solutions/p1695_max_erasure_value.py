from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        accum_sum = defaultdict(int)
        max_sum = 0
        curr_sum = 0
        left = 0

        for num in nums:
            accum_sum[num] += 1
            curr_sum += num
            while accum_sum[num] > 1:
                accum_sum[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum


class TestMaximumUniqueSubarray:
    def test_example1(self):
        nums = [4, 2, 4, 5, 6]
        expected = 17
        s = Solution()
        result = s.maximumUniqueSubarray(nums)
        assert result == expected

    def test_example2(self):
        nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
        expected = 8
        s = Solution()
        result = s.maximumUniqueSubarray(nums)
        assert result == expected
