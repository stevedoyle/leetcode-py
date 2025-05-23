class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


class TestMakeGood:
    def test_make_good(self):
        solution = Solution()
        # Test case 1: Simple case with adjacent duplicates
        assert solution.makeGood("abBAcC") == ""

        # Test case 2: No adjacent duplicates
        assert solution.makeGood("abc") == "abc"

        # Test case 3: All characters are the same
        assert solution.makeGood("aaaa") == "aaaa"

        # Test case 4: Empty string
        assert solution.makeGood("") == ""

        # Test case 5: Mixed case with adjacent duplicates
        assert solution.makeGood("aA") == ""

    def test_example1(self):
        solution = Solution()
        assert solution.makeGood("leEeetcode") == "leetcode"
