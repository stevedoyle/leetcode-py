from utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far) -> int:
            if not node:
                return 0

            left = dfs(node.left, max(max_so_far, node.val))
            right = dfs(node.right, max(max_so_far, node.val))

            result = left + right
            if node.val >= max_so_far:
                result += 1
            return result

        return dfs(root, 0)


class TestGoodNodes:
    def test_example1(self):
        root = [3, 1, 4, 3, None, 1, 5]
        tree = TreeNode.from_list(root)
        expected = 4
        result = Solution().goodNodes(tree)  # type: ignore
        assert result == expected

    def test_example2(self):
        root = [3, 3, None, 4, 2]
        tree = TreeNode.from_list(root)
        expected = 3
        result = Solution().goodNodes(tree)  # type: ignore
        assert result == expected

    def test_example3(self):
        root = [1]
        tree = TreeNode.from_list(root)
        expected = 1
        result = Solution().goodNodes(tree)  # type: ignore
        assert result == expected
