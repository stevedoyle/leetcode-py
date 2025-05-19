from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        result = curr = 0

        for num in nums:
            curr += num
            result += counts[curr - k]
            counts[curr] += 1
        return result


class TestSubarraySum:
    def test_example1(self):
        nums = [1, 1, 1]
        k = 2
        expected = 2
        s = Solution()
        result = s.subarraySum(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 3]
        k = 3
        expected = 2
        s = Solution()
        result = s.subarraySum(nums, k)
        assert result == expected

    def test_example3(self):
        nums = [0, 0, 0]
        k = 0
        expected = 6
        s = Solution()
        result = s.subarraySum(nums, k)
        assert result == expected
