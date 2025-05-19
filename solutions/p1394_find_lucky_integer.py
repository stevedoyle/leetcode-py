from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        lucky_numbers = [num for num, count in counts.items() if num == count]
        return max(lucky_numbers) if lucky_numbers else -1


class TestFindLucky:
    def test_example1(self):
        arr = [2, 2, 3, 4]
        expected = 2
        s = Solution()
        result = s.findLucky(arr)
        assert result == expected

    def test_example2(self):
        arr = [1, 2, 2, 3, 3, 3]
        expected = 3
        s = Solution()
        result = s.findLucky(arr)
        assert result == expected

    def test_example3(self):
        arr = [2, 2, 2, 3, 3]
        expected = -1
        s = Solution()
        result = s.findLucky(arr)
        assert result == expected
