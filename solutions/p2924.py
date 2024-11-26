# Title: Find Champion II
# URL: https://binarysearch.com/problems/Find-Champion-II
# Difficulty: Medium

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0

        played = set([i for i in range(n)])
        stronger = set()
        weaker = set()

        for a, b in edges:
            stronger.add(a)
            weaker.add(b)
            played.discard(a)
            played.discard(b)

        if len(played) != 0:
            print(played)
            return -1

        only_stronger = stronger - weaker
        if len(only_stronger) != 1:
            return -1
        return only_stronger.pop()


class TestFindChampion:
    def test_example1(self):
        n = 3
        edges = [[0, 1], [1, 2]]
        assert Solution().findChampion(n, edges) == 0

    def test_example2(self):
        n = 4
        edges = [[0, 2], [1, 3], [1, 2]]
        assert Solution().findChampion(n, edges) == -1

    def test_example3(self):
        n = 3
        edges = [[0, 1]]
        assert Solution().findChampion(n, edges) == -1
