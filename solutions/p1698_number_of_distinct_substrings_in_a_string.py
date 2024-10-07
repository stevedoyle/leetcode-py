# Title: Number of Distinct Substrings in a String
# URL: https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/
# Difficulty: Medium


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def countDistinct(self, s: str) -> int:
        subs = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subs.add(s[i:j])
        return len(subs)


class TestCountDistinct:
    def test_example1(self):
        s = "aabbaba"
        assert Solution().countDistinct(s) == 21

    def test_example2(self):
        s = "abcdefg"
        assert Solution().countDistinct(s) == 28
