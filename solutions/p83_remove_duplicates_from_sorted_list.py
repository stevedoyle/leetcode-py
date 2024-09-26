# Title: Remove Duplicates from Sorted List
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy

# Problem

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

from typing import Optional

from utils import ListNode, create_linked_list


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
        head = create_linked_list([1, 1, 2])
        expected = create_linked_list([1, 2])
        actual = Solution().deleteDuplicates(head)
        assert actual == expected

    def test_example2(self):
        head = create_linked_list([1, 1, 2, 3, 3])
        expected = create_linked_list([1, 2, 3])
        assert Solution().deleteDuplicates(head) == expected
