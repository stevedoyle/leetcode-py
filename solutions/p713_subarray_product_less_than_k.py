from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


class TestNumSubarrayProductLessThanK:
    def test_example1(self):
        nums = [10, 5, 2, 6]
        k = 100
        expected = 8
        s = Solution()
        result = s.numSubarrayProductLessThanK(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [1, 2, 3]
        k = 0
        expected = 0
        s = Solution()
        result = s.numSubarrayProductLessThanK(nums, k)
        assert result == expected

    def test_example3(self):
        nums = [1, 2, 3]
        k = 6
        expected = 4
        s = Solution()
        result = s.numSubarrayProductLessThanK(nums, k)
        assert result == expected
