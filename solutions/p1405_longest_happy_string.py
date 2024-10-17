# Title: Longest Happy String
# URL: https://leetcode.com/problems/longest-happy-string/
# Difficulty: Medium


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        curra, currb, currc = 0, 0, 0
        totalIterations = a + b + c
        for _ in range(totalIterations):
            if (a >= b and a >= c and curra != 2) or (
                (currb == 2 or currc == 2) and a > 0
            ):
                result += "a"
                a -= 1
                curra += 1
                currb, currc = 0, 0
            elif (b >= a and b >= c and currb != 2) or (
                (curra == 2 or currc == 2) and b > 0
            ):
                result += "b"
                b -= 1
                currb += 1
                curra, currc = 0, 0
            elif (c >= a and c >= b and currc != 2) or (
                (curra == 2 or currb == 2) and c > 0
            ):
                result += "c"
                c -= 1
                currc += 1
                curra, currb = 0, 0
        return result


class TestLongestHappyString:
    def test_example1(self):
        a = 1
        b = 1
        c = 7

        assert Solution().longestDiverseString(a, b, c) == "ccaccbcc"

    def test_example2(self):
        a = 7
        b = 1
        c = 0

        assert Solution().longestDiverseString(a, b, c) == "aabaa"
