from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurrences = list(counts.values())
        return len(occurrences) == len(set(occurrences))


class TestUniqueOccurrences:
    def test_example1(self):
        arr = [1, 2, 2, 1, 1, 3]
        expected = True
        s = Solution()
        result = s.uniqueOccurrences(arr)
        assert result == expected

    def test_example2(self):
        arr = [1, 2]
        expected = False
        s = Solution()
        result = s.uniqueOccurrences(arr)
        assert result == expected

    def test_example3(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        expected = True
        s = Solution()
        result = s.uniqueOccurrences(arr)
        assert result == expected
