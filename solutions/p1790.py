# Title: 1790: Check if One String Swap Can Make Strings Equal
# URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# Difficulty: Easy


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Check if two strings are almost equal by swapping at most one pair of characters.

        Two strings s1 and s2 are considered almost equal if you can make them equal by swapping at most one pair of characters in one of the strings.

        Args:
            s1 (str): The first string to compare.
            s2 (str): The second string to compare.

        Returns:
            bool: True if the strings are almost equal, False otherwise.
        """
        if s1 == s2:
            return True

        diff = tuple((a, b) for a, b in zip(s1, s2) if a != b)

        return len(diff) == 2 and diff[0] == diff[1][::-1]


class TestCheckIfOneStringSwapCanMakeStringsEqual:
    def test_example1(self):
        """Test case where one swap can make the strings equal."""
        s1 = "bank"
        s2 = "kanb"
        assert Solution().areAlmostEqual(s1, s2)

    def test_example2(self):
        """Test case where no swap can make the strings equal."""
        s1 = "attack"
        s2 = "defend"
        assert not Solution().areAlmostEqual(s1, s2)

    def test_example3(self):
        """Test case where the strings are already equal."""
        s1 = "kelb"
        s2 = "kelb"
        assert Solution().areAlmostEqual(s1, s2)
