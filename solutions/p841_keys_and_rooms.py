# Title: Keys and Rooms
# URL: https://leetcode.com/problems/keys-and-rooms/
# Difficulty: Medium

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)


class TestCanVisitAllRooms:
    def test_example1(self):
        rooms = [[1], [2], [3], []]
        assert Solution().canVisitAllRooms(rooms) == True

    def test_example2(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        assert Solution().canVisitAllRooms(rooms) == False
