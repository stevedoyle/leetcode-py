# Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Difficulty: Hard

# Given a string s and an array of strings words of the same length, find all
# starting indices of substring(s) in s which is a concatenation of each word
# in words exactly once and without any intervening characters.
#
# You can return the answer in any order.
# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: The substring starting at index 0 is "barfoo".
# The substring starting at index 9 is "foobar".
#
# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Explanation: There is no concatenated substring.
#
# Example 3:
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation: The substring starting at index 6 is "barfoothe".
# The substring starting at index 9 is "foobar".
# The substring starting at index 12 is "barfoo".
#
# Constraints:
# 1 <= s.length <= 104
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# s consists of lowercase English letters.
# All the strings of words are unique.

from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Edge case: if s is empty or words is empty
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_map = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            seen = defaultdict(int)
            for j in range(word_count):
                word_index = i + j * word_length
                word = s[word_index : word_index + word_length]

                if word in word_map:
                    seen[word] += 1
                    if seen[word] > word_map[word]:
                        break
                else:
                    break
            else:
                result.append(i)

        return result


class TestFindSubstring:
    def test_example_1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        assert Solution().findSubstring(s, words) == expected

    def test_example_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        assert Solution().findSubstring(s, words) == expected

    def test_example_3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        assert Solution().findSubstring(s, words) == expected

    def test_empty_string(self):
        s = ""
        words = ["foo", "bar"]
        expected = []
        assert Solution().findSubstring(s, words) == expected
