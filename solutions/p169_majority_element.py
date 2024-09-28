# Title: Majority Element
# URL: https://leetcode.com/problems/majority-element/
# Difficulty: Easy

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for key in count:
            if count[key] > len(nums) // 2:
                return key
        return -1


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a dictionary to store the count of each element
        count = {}

        # Iterate through the list of numbers
        for num in nums:
            # If the number is not in the dictionary, add it with a count of 1
            if num not in count:
                count[num] = 1
            # If the number is already in the dictionary, increment the count
            else:
                count[num] += 1

        # Iterate through the dictionary
        for key in count:
            # If the count of the number is greater than half the length of the list, return the number
            if count[key] > len(nums) // 2:
                return key
        return -1


# Time Complexity: O(n)
# Space Complexity: O(n)


# New approach
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the list of numbers
        nums.sort()

        # Return the middle element
        return nums[len(nums) // 2]


# Time Complexity: O(n log n)
# Space Complexity: O(1)


# New approach
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a variable to store the majority element
        majority = nums[0]
        count = 1

        # Iterate through the list of numbers
        for num in nums[1:]:
            # If the count is 0, update the majority element
            if count == 0:
                majority = num
                count = 1
            # If the number is the majority element, increment the count
            elif num == majority:
                count += 1
            # If the number is not the majority element, decrement the count
            else:
                count -= 1

        return majority


# Time Complexity: O(n)
# Space Complexity: O(1)


class TestMajorityElement:
    def test_example1(self):
        assert Solution().majorityElement([3, 2, 3]) == 3

    def test_example2(self):
        assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
