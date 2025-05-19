from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        for arr in nums:
            for num in set(arr):
                count[num] += 1

        n = len(nums)
        result = []
        for num, cnt in count.items():
            if cnt == n:
                result.append(num)

        return sorted(result)


class TestIntersection:
    def test_example1(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = []
        s = Solution()
        result = s.intersection(nums)
        assert result == expected

    def test_example2(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        expected = [3]
        s = Solution()
        result = s.intersection(nums)
        assert result == expected

    def test_example3(self):
        nums = [[1, 2], [2, 3], [3, 4]]
        expected = []
        s = Solution()
        result = s.intersection(nums)
        assert result == expected

    def test_example4(self):
        nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
        expected = [3, 4]
        s = Solution()
        result = s.intersection(nums)
        assert result == expected
