from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        result = 0
        odd_count = 0

        for num in nums:
            odd_count += num % 2
            result += counts[odd_count - k]
            counts[odd_count] += 1
        return result


class TestNumberOfSubarrays:
    def test_example1(self):
        nums = [1, 1, 2, 1, 1]
        k = 3
        expected = 2
        s = Solution()
        result = s.numberOfSubarrays(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [2, 4, 6]
        k = 1
        expected = 0
        s = Solution()
        result = s.numberOfSubarrays(nums, k)
        assert result == expected

    def test_example3(self):
        nums = [1, 1, 2, 1, 1]
        k = 2
        expected = 5
        s = Solution()
        result = s.numberOfSubarrays(nums, k)
        assert result == expected

    def test_example4(self):
        nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        k = 2
        expected = 16
        s = Solution()
        result = s.numberOfSubarrays(nums, k)
        assert result == expected
