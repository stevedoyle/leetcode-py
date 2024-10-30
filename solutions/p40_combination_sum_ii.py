# Title: Combination Sum II
# URL: https://leetcode.com/problems/combination-sum-ii/
# Difficulty: Medium

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return  # backtracking
        if target == 0:
            answer.append(path)
            return  # end
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )


class TestCombinationSum2:
    def test_example1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        assert Solution().combinationSum2(candidates, target) == expected

    def test_example2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        assert Solution().combinationSum2(candidates, target) == expected
