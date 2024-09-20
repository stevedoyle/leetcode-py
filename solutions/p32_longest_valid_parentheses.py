# Problem: Longest Valid Parentheses
# URL: https://leetcode.com/problems/longest-valid-parentheses/
# Difficulty: Hard


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length


class TestLongestValidParentheses:
    def test_example1(self):
        s = "(()"
        assert Solution().longestValidParentheses(s) == 2

    def test_example2(self):
        s = ")()())"
        assert Solution().longestValidParentheses(s) == 4

    def test_example3(self):
        s = ""
        assert Solution().longestValidParentheses(s) == 0
