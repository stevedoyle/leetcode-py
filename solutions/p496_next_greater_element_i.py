from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        next_greater = {}

        # Create a mapping of next greater elements for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            result.append(next_greater.get(num, -1))
        return result


class TestNextGreaterElement:
    def test_example1(self):
        assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]

    def test_example2(self):
        assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]

    def test_example3(self):
        assert Solution().nextGreaterElement([1, 2, 3], [3, 2, 1]) == [-1, -1, -1]
