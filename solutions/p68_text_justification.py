# Title: Text Justification
# URL: https://leetcode.com/problems/text-justification/
# Difficulty: Hard

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0
        for word in words:
            if line_length + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += " "
                result.append("".join(line))
                line = []
                line_length = 0
            line.append(word)
            line_length += len(word)
        result.append(" ".join(line).ljust(maxWidth))
        return result


class TestFullJustify:
    def test_example1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = ["This    is    an", "example  of text", "justification.  "]
        assert Solution().fullJustify(words, maxWidth) == expected

    def test_example2(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        maxWidth = 16
        expected = ["What   must   be", "acknowledgment  ", "shall be        "]
        assert Solution().fullJustify(words, maxWidth) == expected
