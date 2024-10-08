# Title: Combination Sum III
# URL: https://leetcode.com/problems/combination-sum-iii/
# Difficulty: Medium

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(target, comb, next_start):
            if target == 0 and len(comb) == k:
                # make a copy of current combination
                # otherwise the combination would be reverted in other branch
                # of backtracking
                results.append(list(comb))
                return
            elif target < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates
            for i in range(next_start, 10):
                comb.append(i)
                backtrack(target - i, comb, i + 1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 1)

        return results


class TestCombinationSum3:
    def test_example1(self):
        k = 3
        n = 7
        expected = [[1, 2, 4]]
        s = Solution()
        result = s.combinationSum3(k, n)
        assert result == expected

    def test_example2(self):
        k = 3
        n = 9
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        s = Solution()
        result = s.combinationSum3(k, n)
        assert result == expected

    def test_example3(self):
        k = 4
        n = 1
        expected = []
        s = Solution()
        result = s.combinationSum3(k, n)
        assert result == expected
