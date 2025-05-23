from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


class TestValidateStackSequences:
    def test_example1(self):
        assert (
            Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True
        )

    def test_example2(self):
        assert (
            Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False
        )

    def test_example3(self):
        assert Solution().validateStackSequences([1], [1]) is True
