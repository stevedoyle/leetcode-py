# Title: H-Index
# URL: https://leetcode.com/problems/h-index/
# Difficulty: Medium

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        h = 0
        for i in range(n):
            h = max(h, min(citations[i], n - i))
        return h


class TestHIndex:
    def test_example1(self):
        citations = [3, 0, 6, 1, 5]
        assert Solution().hIndex(citations) == 3

    def test_example2(self):
        citations = [1, 3, 1]
        assert Solution().hIndex(citations) == 1
