# Title: 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/
# Difficulty: Medium


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a mapping of characters in order to their index
        # This will help in sorting the characters in s based on their order
        # Characters not in order will be sorted to the end
        # by assigning them a value greater than the length of order
        order_map = {char: i for i, char in enumerate(order)}
        sorted_s = sorted(s, key=lambda x: order_map.get(x, len(order)))
        return "".join(sorted_s)


class TestCustomSortString:
    def test_example1(self):
        order = "cba"
        s = "abcd"
        expected = "cbad"
        sol = Solution()
        result = sol.customSortString(order, s)
        assert result == expected

    def test_example2(self):
        order = "bcafg"
        s = "abcd"
        expected = "bcad"
        sol = Solution()
        result = sol.customSortString(order, s)
        assert result == expected
