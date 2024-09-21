# Title: Remove Duplicates from Sorted List
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy

# Problem

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False

        if self.val != other.val:
            return False

        if self.next is None and other.next is None:
            return True

        return self.next == other.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current = head
        while current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


class TestDeleteDuplicates:
    def test_example1(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        expected = ListNode(1, ListNode(2))
        actual = Solution().deleteDuplicates(head)
        assert actual == expected

    def test_example2(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        assert Solution().deleteDuplicates(head) == expected
