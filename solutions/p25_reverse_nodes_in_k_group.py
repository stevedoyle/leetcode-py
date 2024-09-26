# Title: 25. Reverse Nodes in k-Group
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Difficulty: Hard

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        def reverse_linked_list(head, k):
            prev = None
            current = head
            for _ in range(k):
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = get_length(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while length >= k:
            tail = prev.next
            for _ in range(k - 1):
                tail = tail.next
            next = tail.next
            tail.next = None
            prev.next = reverse_linked_list(prev.next, k)
            tail = prev.next
            while tail.next:
                tail = tail.next
            tail.next = next
            prev = tail
            length -= k

        return dummy.next


class TestReverseKGroup:
    def test_example1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        k = 2
        expected = list_to_linked_list([2, 1, 4, 3, 5])
        assert Solution().reverseKGroup(head, k) == expected
