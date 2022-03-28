"""See the README.html file"""
from typing import Optional

from utils import TreeNode


class Solution:
    """Solution for the problem as used by leetcode solver."""

    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """Sums the current node and all nodes below recursively."""
        result_node = TreeNode()
        if root1 is not None and root2 is not None:
            result_node.val = root1.val + root2.val
            result_node.left = self.mergeTrees(root1.left, root2.left)
            result_node.right = self.mergeTrees(root1.right, root2.right)
        elif root1 is not None and root2 is None:
            result_node = root1
        elif root1 is None and root2 is not None:
            result_node = root2
        elif root1 is None and root2 is None:
            return
        return result_node


if __name__ == "__main__":
    r1 = [1]
    r2 = [1, 2]
    tree1 = TreeNode(r1)
    tree2 = TreeNode(r2)
    merged = Solution().mergeTrees(tree1, tree2)

    r1 = [1, 3, 2, 5]
    r2 = [2, 1, 3, None, 4, None, 7]
    tree1 = TreeNode(r1)
    tree2 = TreeNode(r2)
    merged = Solution().mergeTrees(tree1, tree2)
