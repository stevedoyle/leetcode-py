# Title: Insert Delete GetRandom O(1)
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Difficulty: Medium

import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


class TestRandomizedSet:
    def test_example1(self):
        obj = RandomizedSet()
        assert obj.insert(1)
        assert not obj.remove(2)
        assert obj.insert(2)
        assert obj.getRandom() in [1, 2]
        assert obj.remove(1)
        assert not obj.insert(2)
        assert obj.getRandom() == 2
