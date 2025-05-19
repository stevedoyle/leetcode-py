from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]
        for num in nums[1:]:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


class TestNumArray:
    def test_example1(self):
        nums = [-2, 0, 3, -5, 2, -1]
        num_array = NumArray(nums)
        assert num_array.sumRange(0, 2) == 1
        assert num_array.sumRange(2, 5) == -1
        assert num_array.sumRange(0, 5) == -3

    def test_example2(self):
        nums = [1]
        num_array = NumArray(nums)
        assert num_array.sumRange(0, 0) == 1
