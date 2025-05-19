from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(num for num, count in counts.items() if count == 1)


class TestSumOfUnique:
    def test_example1(self):
        nums = [1, 2, 3, 2]
        expected = 4
        s = Solution()
        result = s.sumOfUnique(nums)
        assert result == expected

    def test_example2(self):
        nums = [1, 1, 1, 1, 1]
        expected = 0
        s = Solution()
        result = s.sumOfUnique(nums)
        assert result == expected

    def test_example3(self):
        nums = [1, 2, 3, 4, 5]
        expected = 15
        s = Solution()
        result = s.sumOfUnique(nums)
        assert result == expected
