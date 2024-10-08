# Title: 1963. Minimum Number of Swaps to Make the String Balanced
# URL: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# Difficulty: Medium


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minSwaps(self, s: str) -> int:
        stack_size = 0
        for c in s:
            if c == "[":
                stack_size += 1
            else:
                if stack_size > 0:
                    stack_size -= 1
        return (stack_size + 1) // 2


class TestMinSwaps:
    def test_example1(self):
        s = "][]["
        assert Solution().minSwaps(s) == 1

    def test_example2(self):
        s = "]]][[["
        assert Solution().minSwaps(s) == 2

    def test_example3(self):
        s = "[]"
        assert Solution().minSwaps(s) == 0
