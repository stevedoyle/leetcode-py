from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val

    def __hash__(self):
        return id(self)

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


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @classmethod
    def from_list(cls, arr):
        if not arr:
            return None
        nodes = [Node(val=i + 1) for i in range(len(arr))]
        for i, neighbors in enumerate(arr):
            for neighbor in neighbors:
                nodes[i].neighbors.append(nodes[neighbor - 1])
        return nodes[0]

    def to_list(self):
        if not self:
            return []

        result = []
        visited = {}

        def dfs(node):
            if node.val in visited:
                return
            visited[node.val] = [x.val for x in node.neighbors]
            for neighbor in node.neighbors:
                dfs(neighbor)

        dfs(self)
        for k in sorted(visited.keys()):
            result.append(visited[k])

        return result


class TestNode:
    def test_from_list(self):
        input = [[2, 4], [1, 3], [2, 4], [1, 3]]
        expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
        result = Node.from_list(input)
        result = result.to_list() if result else None
        assert result == expected

    def test_to_list(self):
        input = Node(1, [Node(2), Node(3)])
        expected = [[2, 3], [], []]
        result = input.to_list()
        assert result == expected

    def test_to_list_single_node(self):
        input = Node(1)
        expected = [[]]
        result = input.to_list()
        assert result == expected


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_list(self) -> list:
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                if current.left or current.right:
                    queue.append(current.left)
                    queue.append(current.right)
            else:
                result.append(None)
        return result


def create_tree(arr: list) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root


class TestTreeNode:
    def test_create_tree(self):
        input = [1, 2, 3, None, 4, 5, None]
        expected = [1, 2, 3, None, 4, 5, None]
        result = create_tree(input)
        result = result.to_list() if result else None
        assert result == expected
