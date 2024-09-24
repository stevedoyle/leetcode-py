# Title: Find the Length of Longest Common Prefix
# URL: https://leetcode.com/problems/find-the-length-of-longest-common-prefix/
# Difficulty: Medium

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # build a hash set of all the possible prefixes or arr1
        arr1_prefixes = self.prefixes(arr1)

        # find the longest common prefix
        longest_common_prefix = 0
        for value in arr2:
            value_str = str(value)
            for i in range(len(value_str)):
                if value_str[: i + 1] in arr1_prefixes:
                    longest_common_prefix = max(longest_common_prefix, i + 1)
                else:
                    break

        return longest_common_prefix

    def prefixes(self, values: List[int]) -> set:
        prefix = set()
        for value in values:
            value_str = str(value)
            for i in range(len(value_str)):
                prefix.add(value_str[: i + 1])
        return prefix


class TestLongestCommonPrefix:
    def test_example1(self):
        assert Solution().longestCommonPrefix([1, 10, 100], [1000]) == 3

    def test_example2(self):
        assert Solution().longestCommonPrefix([1, 2, 3], [4, 4, 4]) == 0

    def test_prefixes(self):
        assert Solution().prefixes([1234]) == {"1", "12", "123", "1234"}
