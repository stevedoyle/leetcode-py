class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


class TestRemoveStars:
    def test_example1(self):
        assert Solution().removeStars("leet**cod*e") == "lecoe"

    def test_example2(self):
        assert Solution().removeStars("erase*****") == ""
