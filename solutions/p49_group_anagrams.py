# Title: 49. Group Anagrams
# URL: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())


class TestGroupAnagrams:
    def compare(self, actual: List[List[str]], expected: List[List[str]]):
        a = sorted([sorted(x) for x in actual])
        b = sorted([sorted(x) for x in expected])
        return a == b

    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["tan", "nat"], ["ate", "eat", "tea"]]
        actual = Solution().groupAnagrams(strs)
        assert self.compare(actual, expected)

    def test_example2(self):
        strs = [""]
        expected = [[""]]
        actual = Solution().groupAnagrams(strs)
        assert self.compare(actual, expected)

    def test_example3(self):
        strs = ["a"]
        expected = [["a"]]
        actual = Solution().groupAnagrams(strs)
        assert self.compare(actual, expected)
