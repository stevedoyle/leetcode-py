from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta_array = [0] * (len(nums) + 1)
        for left, right in queries:
            if left < 0 or right >= len(nums) or left > right:
                return False
            delta_array[left] += 1
            if right + 1 < len(delta_array):
                delta_array[right + 1] -= 1

        op_counts = []
        curr = 0
        for i in range(len(nums)):
            curr += delta_array[i]
            op_counts.append(curr)
        for ops, target in zip(op_counts, nums):
            if ops < target:
                print(f"ops: {ops}, target: {target}")
                return False
        return True

    def isZeroArrayTooSlow(self, nums: List[int], queries: List[List[int]]) -> bool:
        for query in queries:
            left, right = query
            if left < 0 or right >= len(nums) or left > right:
                return False
            for i in range(left, right + 1):
                nums[i] = max(nums[i] - 1, 0)
        return all(num == 0 for num in nums)


class TestZeroArray:
    def test_example1(self):
        nums = [1, 0, 1]
        queries = [[0, 2]]
        expected = True
        s = Solution()
        result = s.isZeroArray(nums, queries)
        assert result == expected

    def test_example2(self):
        nums = [4, 3, 2, 1]
        queries = [[1, 3], [0, 2]]
        expected = False
        s = Solution()
        result = s.isZeroArray(nums, queries)
        assert result == expected
