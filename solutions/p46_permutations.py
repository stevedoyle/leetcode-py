from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
        """
        result = []
        self._backtrack(nums, [], result)
        return result

    def _backtrack(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path)
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self._backtrack(nums, path + [nums[i]], result)
        return

    def permuteIterative(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
        """
        result = []
        stack = [(nums, [])]
        while stack:
            nums, path = stack.pop()
            if len(path) == len(nums):
                result.append(path)
                continue
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                stack.append((nums, path + [nums[i]]))
        return result


class TestPermutations:
    def test_example1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        s = Solution()
        result = s.permute(nums)
        assert sorted(result) == sorted(expected)

    def test_example2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        s = Solution()
        result = s.permute(nums)
        assert sorted(result) == sorted(expected)

    def test_example3(self):
        nums = [1]
        expected = [[1]]
        s = Solution()
        result = s.permute(nums)
        assert sorted(result) == sorted(expected)
