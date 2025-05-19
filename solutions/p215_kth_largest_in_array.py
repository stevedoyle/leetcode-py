from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element in an unsorted array.
        :param nums: List[int] - List of integers
        :param k: int - The kth position to find
        :return: int - The kth largest element
        """
        nums.sort(reverse=True)
        return nums[k - 1]


class TestFindKthLargest:
    def test_example1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        s = Solution()
        result = s.findKthLargest(nums, k)
        assert result == expected

    def test_example2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        s = Solution()
        result = s.findKthLargest(nums, k)
        assert result == expected

    def test_example3(self):
        nums = [1]
        k = 1
        expected = 1
        s = Solution()
        result = s.findKthLargest(nums, k)
        assert result == expected
