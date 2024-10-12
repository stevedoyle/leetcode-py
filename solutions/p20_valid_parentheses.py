# Title: Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


class TestIsValid:
    def test_example1(self):
        s = "()"
        assert Solution().isValid(s)

    def test_example2(self):
        s = "()[]{}"
        assert Solution().isValid(s)

    def test_example3(self):
        s = "(]"
        assert not Solution().isValid(s)

    def test_example4(self):
        s = "([)]"
        assert not Solution().isValid(s)
