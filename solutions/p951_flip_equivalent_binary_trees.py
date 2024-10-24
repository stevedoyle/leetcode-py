# Title: 951. Flip Equivalent Binary Trees
# URL: https://leetcode.com/problems/flip-equivalent-binary-trees/
# Difficulty: Medium

from utils import TreeNode, create_tree
from typing import Optional


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        node_pair_stack = []
        node_pair_stack.append((root1, root2))

        while node_pair_stack:
            node1, node2 = node_pair_stack.pop()
            if not self.check_node_values(node1, node2):
                return False

            if not node1 and not node2:
                continue

            if self.check_node_values(
                node1.left, node2.left
            ) and self.check_node_values(node1.right, node2.right):
                node_pair_stack.append((node1.left, node2.left))
                node_pair_stack.append((node1.right, node2.right))
            elif self.check_node_values(
                node1.left, node2.right
            ) and self.check_node_values(node1.right, node2.left):
                node_pair_stack.append((node1.left, node2.right))
                node_pair_stack.append((node1.right, node2.left))
            else:
                return False
        return True

    def check_node_values(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return True
        return False


class TestFlipEquiv:
    def test_example1(self):
        root1 = create_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8])
        root2 = create_tree([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])
        assert Solution().flipEquiv(root1, root2)

    def test_example2(self):
        root1 = create_tree([])
        root2 = create_tree([])
        assert Solution().flipEquiv(root1, root2)

    def test_example3(self):
        root1 = create_tree([])
        root2 = create_tree([1])
        assert not Solution().flipEquiv(root1, root2)
