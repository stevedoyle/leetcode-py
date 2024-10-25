# Title: Add Two Numbers
# URL: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium

from typing import Optional
from utils import ListNode, create_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
        return dummy.next


class TestAddTwoNumbers:
    def test_exmple1(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        expected = [7, 0, 8]
        result = Solution().addTwoNumbers(l1, l2).to_list()
        assert result == expected

    def test_exmple2(self):
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        expected = [0]
        result = Solution().addTwoNumbers(l1, l2).to_list()
        assert result == expected

    def test_exmple3(self):
        l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = create_linked_list([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        result = Solution().addTwoNumbers(l1, l2).to_list()
        assert result == expected
