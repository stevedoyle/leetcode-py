# Title: Minimum Changes to Make a Binary String Beautiful
# URL: https://leetcode.com/problems/minimum-changes-to-make-a-binary-string-beautiful/
# Difficulty: Medium


class Solution:
    def minChanges(self, s: str) -> int:
        if not s or len(s) % 2 == 1:
            return 0
        min_changes_required = 0

        # Check pairs of characters (i, i+1) with step size 2
        for i in range(0, len(s), 2):
            # If the characters in the current pair don't match,
            # we need one change to make them equal.
            if s[i] != s[i + 1]:
                min_changes_required += 1
        return min_changes_required


class TestMinChanges:
    def test_example1(self):
        s = "1001"
        assert Solution().minChanges(s) == 2

    def test_example2(self):
        s = "10"
        assert Solution().minChanges(s) == 1

    def test_example3(self):
        s = "0000"
        assert Solution().minChanges(s) == 0
