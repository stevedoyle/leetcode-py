# Title: 228. Summary Ranges
# URL: https://leetcode.com/problems/summary-ranges/
# Difficulty: Medium

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                ranges.append(str(start) + "->" + str(nums[i]))
            else:
                ranges.append(str(nums[i]))

            i += 1

        return ranges


class TestSummaryRanges:
    def test_example1(self):
        nums = [0, 1, 2, 4, 5, 7]
        expected = ["0->2", "4->5", "7"]
        assert Solution().summaryRanges(nums) == expected

    def test_example2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        expected = ["0", "2->4", "6", "8->9"]
        assert Solution().summaryRanges(nums) == expected
