# Title: Sqrt(x)
# URL: https://leetcode.com/problems/sqrtx/
# Difficulty: Easy


class Solution:
    def mySqrt(self, x: int) -> int:
        # Base case
        if x == 0 or x == 1:
            return x

        # Binary search to find the square root
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class TestMySqrt:
    def test_example1(self):
        assert Solution().mySqrt(4) == 2

    def test_example2(self):
        assert Solution().mySqrt(8) == 2
