from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freqs = Counter(nums)
        good_pairs = 0

        for count in freqs.values():
            good_pairs += count * (count - 1) // 2
        return good_pairs


class TestNumIdenticalPairs:
    def test_example1(self):
        nums = [1, 2, 3, 1, 1, 3]
        expected = 4
        s = Solution()
        result = s.numIdenticalPairs(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 1, 1, 1]
        expected = 6
        s = Solution()
        result = s.numIdenticalPairs(nums)
        assert result == expected

    def test_example3(self):
        nums = [1, 2, 3]
        expected = 0
        s = Solution()
        result = s.numIdenticalPairs(nums)
        assert result == expected
