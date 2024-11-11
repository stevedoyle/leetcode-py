# Title: Prime Subtraction Operation
# URL: https://leetcode.com/problems/prime-subtraction-operation/
# Difficulty: Medium

from typing import List


class Solution:
    def is_prime(self, num: int) -> bool:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        maxElement = max(nums)

        # Store the rpeviousPrime array
        previous_prime = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            previous_prime[i] = previous_prime[i - 1]
            if self.is_prime(i):
                previous_prime[i] = i

        for i, num in enumerate(nums):
            if i == 0:
                bound = num
            else:
                bound = num - nums[i - 1]

            if bound <= 0:
                return False

            largest_prime = previous_prime[bound - 1]
            nums[i] -= largest_prime

        return True


class TestPrimeSubOperation:
    def test_example1(self):
        assert Solution().primeSubOperation([4, 9, 6, 10])

    def test_example2(self):
        assert Solution().primeSubOperation([6, 8, 11, 12])

    def test_example3(self):
        assert not Solution().primeSubOperation([5, 8, 3])
