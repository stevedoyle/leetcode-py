# Title: 921. Minimum Add to Make Parentheses Valid
# URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Difficulty: Medium


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        unbalanced_count = 0
        for ch in s:
            if ch == "(":
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    unbalanced_count += 1

        return open_count + unbalanced_count

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minAddToMakeValidv2(self, s: str) -> int:
        stack = []
        open_count = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    open_count += 1

        return open_count + len(stack)


class TestMinAdd:
    def test_example1(self):
        s = "())"
        assert Solution().minAddToMakeValid(s) == 1
        assert Solution().minAddToMakeValidv2(s) == 1

    def test_example2(self):
        s = "((("
        assert Solution().minAddToMakeValid(s) == 3
        assert Solution().minAddToMakeValidv2(s) == 3
