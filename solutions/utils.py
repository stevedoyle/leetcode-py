# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next

    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head
