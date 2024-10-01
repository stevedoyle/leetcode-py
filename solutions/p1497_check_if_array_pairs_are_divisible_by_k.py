# Title: Check If Array Pairs Are Divisible by k
# URL: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
# Difficulty: Medium

from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # (x + y) % k = 0 ... for every pair (x,y)
        # => x % k = a; y % k = b
        # => b = k - a
        remainder_count = [0] * k
        for num in arr:
            remainder_count[num % k] += 1

        if remainder_count[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False

        return True


class TestCanArrange:
    def test_example1(self):
        arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
        k = 5
        assert Solution().canArrange(arr, k)

    def test_example2(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 7
        assert Solution().canArrange(arr, k)

    def test_example3(self):
        arr = [1, 2, 3, 4, 5, 6]
        k = 10
        assert not Solution().canArrange(arr, k)
