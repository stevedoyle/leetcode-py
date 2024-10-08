# Title: 39. Combination Sum
# URL: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        result = []
        backtrack(0, target, [])
        return result


class TestCombinationSum:
    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        s = Solution()
        result = s.combinationSum(candidates, target)
        assert result == expected

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        s = Solution()
        result = s.combinationSum(candidates, target)
        assert result == expected

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        s = Solution()
        result = s.combinationSum(candidates, target)
        assert result == expected
