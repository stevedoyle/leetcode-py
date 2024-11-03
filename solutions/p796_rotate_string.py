class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False

        if n == 0:
            return True

        for i in range(n):
            if s[i:] + s[:i] == goal:
                return True
        return False


class TestRotateString:
    def test_example1(self):
        s = "abcde"
        goal = "cdeab"
        assert Solution().rotateString(s, goal)

    def test_example2(self):
        s = "abcde"
        goal = "abced"
        assert not Solution().rotateString(s, goal)
