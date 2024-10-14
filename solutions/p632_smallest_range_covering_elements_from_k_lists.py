# Title: Smallest Range Covering Elements from K Lists
# URL: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Difficulty: Hard

from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize variables
        n = len(nums)
        next = [0] * n
        min_range = float("inf")
        min_range_start = 0
        min_range_end = 0
        max_val = float("-inf")
        min_heap = []

        # Insert the first element of each list to the min heap
        for i in range(n):
            heapq.heappush(min_heap, (nums[i][0], i))
            max_val = max(max_val, nums[i][0])
            next[i] = 1

        # Iterate until one of the list is exhausted
        while True:
            # Get the minimum value from the min heap
            min_val, min_val_list = heapq.heappop(min_heap)

            # Check if the range is smaller than the current minimum range
            if max_val - min_val < min_range:
                min_range = max_val - min_val
                min_range_start = min_val
                min_range_end = max_val

            # Check if the list is exhausted
            if next[min_val_list] == len(nums[min_val_list]):
                break

            # Insert the next element of the list to the min heap
            heapq.heappush(
                min_heap, (nums[min_val_list][next[min_val_list]], min_val_list)
            )
            max_val = max(max_val, nums[min_val_list][next[min_val_list]])
            next[min_val_list] += 1

        return [min_range_start, min_range_end]


class TestSmallestRange:
    def test_example1(self):
        nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        expected = [20, 24]
        assert Solution().smallestRange(nums) == expected

    def test_example2(self):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        expected = [1, 1]
        assert Solution().smallestRange(nums) == expected
