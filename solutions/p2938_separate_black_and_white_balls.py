# Title: Separate Black and White Balls
# Link: https://leetcode.com/problems/separate-black-and-white-balls/
# Difficulty: Medium


class Solution:
    def minimumSteps(self, s: str) -> int:
        white_position = 0
        total_swaps = 0

        for i, char in enumerate(s):
            if char == "0":
                total_swaps += i - white_position
                white_position += 1

        return total_swaps

    def minimumStepsTooSlow(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0

        steps = 0
        modified = True
        balls = list(s)

        while modified:
            modified = False
            for i in range(1, n):
                if balls[i - 1] == "1" and balls[i] == "0":
                    balls[i - 1], balls[i] = balls[i], balls[i - 1]
                    steps += 1
                    modified = True

        return steps


class TestMinSteps:
    def test_example1(self):
        s = "101"
        expected = 1
        assert Solution().minimumSteps(s) == expected
        assert Solution().minimumStepsTooSlow(s) == expected

    def test_example2(self):
        s = "100"
        expected = 2
        assert Solution().minimumSteps(s) == expected
        assert Solution().minimumStepsTooSlow(s) == expected

    def test_example3(self):
        s = "0111"
        expected = 0
        assert Solution().minimumSteps(s) == expected
        assert Solution().minimumStepsTooSlow(s) == expected

    def test_example4(self):
        s = "01110"
        expected = 3
        assert Solution().minimumSteps(s) == expected
        assert Solution().minimumStepsTooSlow(s) == expected
