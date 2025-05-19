from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_freqs[:k]]


class TestTopKFrequent:
    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        s = Solution()
        result = s.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)

    def test_example2(self):
        nums = [1]
        k = 1
        expected = [1]
        s = Solution()
        result = s.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)

    def test_example3(self):
        nums = [1, 2]
        k = 2
        expected = [1, 2]
        s = Solution()
        result = s.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)
