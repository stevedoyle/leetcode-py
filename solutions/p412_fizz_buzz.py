# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(f"{i}")
        return answer


class TestFizzbBuzz:
    def testFizzBuzz1(self):
        want = ["1", "2", "Fizz"]
        sln = Solution()
        assert want == sln.fizzBuzz(3)
