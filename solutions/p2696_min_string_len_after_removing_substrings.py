# Title: 2696. Minimize the Length of a String After Removing Similar Substrings
# URL: https://leetcode.com/problems/minimum_string_length_after_removing_substrings.html
# Difficulty: Medium


class Solution:
    def minLength(self, s: str) -> int:
        substrings = ["AB", "CD"]
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 2:
                if "".join(stack[-2:]) in substrings:
                    stack.pop()
                    stack.pop()
        return len(stack)

    def minLength2(self, s: str) -> int:
        modified = True
        while modified:
            modified = False
            for sub in ["AB", "CD"]:
                i = s.find(sub)
                if i != -1:
                    s = s[:i] + s[i + 2 :]
                    modified = True
        return len(s)


class TestMinLength:
    def test_example1(self):
        s = "ABFCACDB"
        assert Solution().minLength(s) == 2

    def test_example2(self):
        s = "ACBBD"
        assert Solution().minLength(s) == 5

    def test_v2_example1(self):
        s = "ABFCACDB"
        assert Solution().minLength2(s) == 2

    def test_v2_example2(self):
        s = "ACBBD"
        assert Solution().minLength2(s) == 5
