# Title: Minimum Array End
# URL: https://leetcode.com/problems/minimum-array-end/
# Difficulty: Medium


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x
        for _ in range(1, n):
            result = (result + 1) | x

        return result


class TestMinEnd:
    def test_example1(self):
        assert Solution().minEnd(3, 4) == 6

    def test_example2(self):
        assert Solution().minEnd(2, 7) == 15
