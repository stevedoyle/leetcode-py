from typing import Optional
from utils import ListNode, create_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        if slow_prev:
            slow_prev.next = slow.next
        else:  # if the list has only one node
            head = head.next
        return head


class TestDeleteMiddle:
    def test_example1(self):
        head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
        expected = create_linked_list([1, 3, 4, 1, 2, 6])
        s = Solution()
        result = s.deleteMiddle(head)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )

    def test_example2(self):
        head = create_linked_list([1, 2, 3, 4])
        expected = create_linked_list([1, 2, 4])
        s = Solution()
        result = s.deleteMiddle(head)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )
