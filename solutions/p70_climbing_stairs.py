# Title: Climbing Stairs
# URL: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # Fibonacci sequence
        # The number of ways to reach the n-th step is the sum of the ways to
        # reach the (n-1)-th step and the ways to reach the (n-2)-th step.
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

    def climbStairsRecursive(self, n: int) -> int:
        if n <= 2:
            return n

        return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)

    def climbStairsRecursiveMemo(self, n: int) -> int:
        memo = {}

        def climbStairsRecursiveMemoHelper(n: int) -> int:
            if n in memo:
                return memo[n]

            if n <= 2:
                return n

            memo[n] = climbStairsRecursiveMemoHelper(
                n - 1
            ) + climbStairsRecursiveMemoHelper(n - 2)
            return memo[n]

        return climbStairsRecursiveMemoHelper(n)


class TestClimbStairs:
    def test_example1(self):
        n = 2
        assert Solution().climbStairs(n) == 2

    def test_example2(self):
        n = 3
        assert Solution().climbStairs(n) == 3

    def test_recursive_example1(self):
        n = 2
        assert Solution().climbStairsRecursive(n) == 2

    def test_recursive_example2(self):
        n = 3
        assert Solution().climbStairsRecursive(n) == 3

    def test_recursive_memo_example1(self):
        n = 2
        assert Solution().climbStairsRecursiveMemo(n) == 2

    def test_recursive_memo_example2(self):
        n = 3
        assert Solution().climbStairsRecursiveMemo(n) == 3
