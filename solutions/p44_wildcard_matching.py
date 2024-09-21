# Title: 44. Wildcard Matching
# URL: https://leetcode.com/problems/wildcard-matching/
# Difficulty: Hard


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(1, m + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]


class TestIsMatch:
    def test_example1(self):
        s = "aa"
        p = "a"
        assert not Solution().isMatch(s, p)

    def test_example2(self):
        s = "aa"
        p = "*"
        assert Solution().isMatch(s, p)

    def test_example3(self):
        s = "cb"
        p = "?a"
        assert not Solution().isMatch(s, p)