from typing import Optional
from utils import ListNode, create_linked_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        for _ in range(n):
            if right:
                right = right.next

        if not right:
            return head.next

        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head


class TestRemoveNthFromEnd:
    def test_example1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected = create_linked_list([1, 2, 3, 5])
        s = Solution()
        result = s.removeNthFromEnd(head, n)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )

    def test_example2(self):
        head = create_linked_list([1])
        n = 1
        expected = None
        s = Solution()
        result = s.removeNthFromEnd(head, n)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )

    def test_example3(self):
        head = create_linked_list([1, 2])
        n = 1
        expected = create_linked_list([1])
        s = Solution()
        result = s.removeNthFromEnd(head, n)
        assert (result.to_list() if result else None) == (
            expected.to_list() if expected else None
        )
