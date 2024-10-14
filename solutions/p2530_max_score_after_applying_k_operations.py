# Title: Maximal Score After Applying K Operations
# URL: https://leetcode.com/problems/maximal-score-after-applying-k-operations/
# Difficulty: Medium

from typing import List
from math import ceil
import heapq


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        max_heap = []

        for num in nums:
            # Store the negative of the number to make it a max heap
            heapq.heappush(max_heap, -num)

        while k > 0:
            k -= 1
            # Pop the max number from the heap and negate it to get the original number
            max_num = -heapq.heappop(max_heap)
            score += max_num
            heapq.heappush(max_heap, -ceil(max_num / 3))

        return score

    # Time complexity: O(k * n)
    # Space complexity: O(1)
    def maxKelements_too_slow(self, nums: List[int], k: int) -> int:
        score = 0

        for _ in range(k):
            # Do the operation on the max number in the array
            max_num_idx = nums.index(max(nums))
            score += nums[max_num_idx]
            nums[max_num_idx] = ceil(nums[max_num_idx] / 3)

        return score


class TestMaxKElements:
    def test_example1(self):
        nums = [10, 10, 10, 10, 10]
        k = 5
        expected = 50
        assert Solution().maxKelements(nums, k) == expected
        assert Solution().maxKelements_too_slow(nums, k) == expected

    def test_example2(self):
        nums = [1, 10, 3, 3, 3]
        k = 3
        expected = 17
        assert Solution().maxKelements(nums, k) == expected
        assert Solution().maxKelements_too_slow(nums, k) == expected
