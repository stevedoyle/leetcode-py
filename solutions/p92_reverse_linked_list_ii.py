# Title: 92. Reverse Linked List II
# URL: https://leetcode.com/problems/reverse-linked-list-ii/
# Difficulty: Medium

from typing import Optional
from utils import ListNode, create_linked_list


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


class TestReverseBetween:
    def test_example1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        left = 2
        right = 4
        expected = [1, 4, 3, 2, 5]
        assert Solution().reverseBetween(head, left, right).to_list() == expected

    def test_example2(self):
        head = create_linked_list([5])
        left = 1
        right = 1
        expected = [5]
        assert Solution().reverseBetween(head, left, right).to_list() == expected
