from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # If the top of the stack is smaller then it will explode
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # If they are equal, both explode
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                # If the top of the stack is larger, the current asteroid explodes
                else:
                    break
            else:
                # If the loop didn't break, it means the asteroid is safe
                stack.append(asteroid)
        return stack


class TestAsteroidCollision:
    def test_example1(self):
        assert Solution().asteroidCollision([5, 10, -5]) == [5, 10]

    def test_example2(self):
        assert Solution().asteroidCollision([8, -8]) == []

    def test_example3(self):
        assert Solution().asteroidCollision([10, 2, -5]) == [10]
