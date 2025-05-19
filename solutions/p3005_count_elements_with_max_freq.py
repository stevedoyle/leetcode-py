from typing import List
from collections import defaultdict


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        max_freq = 0

        for num in nums:
            freqs[num] += 1
            max_freq = max(max_freq, freqs[num])

        total = 0
        for num, count in freqs.items():
            if count == max_freq:
                total += count
        return total


class TestMaxFrequencyElements:
    def test_example1(self):
        nums = [1, 2, 2, 3, 1, 4]
        expected = 4
        s = Solution()
        result = s.maxFrequencyElements(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 3, 4, 5]
        expected = 5
        s = Solution()
        result = s.maxFrequencyElements(nums)
        assert result == expected
