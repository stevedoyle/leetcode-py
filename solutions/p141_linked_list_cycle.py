# Title: Linked List Cycle
# URL: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
from utils import ListNode, create_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

    def hasCycleV2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class TestHasCycle:
    def test_example1(self):
        head = create_linked_list([3, 2, 0, -4])
        head.next.next.next.next = head.next
        assert Solution().hasCycle(head)
        assert Solution().hasCycleV2(head)

    def test_example2(self):
        head = create_linked_list([1, 2])
        head.next.next = head
        assert Solution().hasCycle(head)
        assert Solution().hasCycleV2(head)

    def test_example3(self):
        head = create_linked_list([1])
        assert not Solution().hasCycle(head)
        assert not Solution().hasCycleV2(head)

    def test_example4(self):
        head = None
        assert not Solution().hasCycle(head)
        assert not Solution().hasCycleV2(head)
