# Title: Remove Duplicate Letters
# URL: https://leetcode.com/problems/remove-duplicate-letters/
# Difficulty: Medium


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    stack.pop()
                stack.append(c)

        return "".join(stack)


class TestRemoveDuplicates:
    def test_example1(self):
        s = "bcabc"
        assert Solution().removeDuplicateLetters(s) == "abc"

    def test_example2(self):
        s = "cbacdcbc"
        assert Solution().removeDuplicateLetters(s) == "acdb"
