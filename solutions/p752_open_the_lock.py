# Title: Open the Lock
# URL: https://leetcode.com/problems/open-the-lock/
# Difficulty: Medium

from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        deadends = set(deadends)
        queue = ["0000"]
        steps = 0

        while queue:
            new_queue = []
            for lock in queue:
                if lock == target:
                    return steps
                if lock in deadends:
                    continue
                if lock in visited:
                    continue
                visited.add(lock)
                for i in range(4):
                    # next combinations by increasing and decreasing each digit by 1
                    for j in [-1, 1]:
                        new_lock = (
                            lock[:i] + str((int(lock[i]) + j) % 10) + lock[i + 1 :]
                        )
                        new_queue.append(new_lock)
            queue = new_queue
            steps += 1
        return -1


class TestOpenLock:
    def test_example1(self):
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        target = "0202"
        expected = 6
        assert Solution().openLock(deadends, target) == expected

    def test_example2(self):
        deadends = ["8888"]
        target = "0009"
        expected = 1
        assert Solution().openLock(deadends, target) == expected

    def test_example3(self):
        deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
        target = "8888"
        expected = -1
        assert Solution().openLock(deadends, target) == expected
