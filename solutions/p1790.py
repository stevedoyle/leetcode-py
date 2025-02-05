# Title: 1790: Check if One String Swap Can Make Strings Equal
# URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# Difficulty: Easy


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff = [(a, b) for a, b in zip(s1, s2) if a != b]

        return len(diff) == 2 and diff[0] == diff[1][::-1]


class TestCheckIfOneStringSwapCanMakeStringsEqual:
    def test_example1(self):
        s1 = "bank"
        s2 = "kanb"
        assert Solution().areAlmostEqual(s1, s2)

    def test_example2(self):
        s1 = "attack"
        s2 = "defend"
        assert not Solution().areAlmostEqual(s1, s2)

    def test_example3(self):
        s1 = "kelb"
        s2 = "kelb"
        assert Solution().areAlmostEqual(s1, s2)
