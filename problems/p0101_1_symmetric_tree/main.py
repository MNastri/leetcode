from typing import Optional

from utils import (
    is_symmetric_trees,
    TreeNode,
)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return self._is_symmetric_trees(root.left, root.right)
        return root and is_symmetric_trees(root.left, root.right)

    # def _is_symmetric_trees(
    #     self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    # ) -> bool:
    #     if root1 and root2:
    #         return (
    #             root1.val == root2.val
    #             and self._is_symmetric_trees(root1.left, root2.right)
    #             and self._is_symmetric_trees(root1.right, root2.left)
    #         )
    #     if root1 is None and root2 is None:
    #         return True
    #     return False


if __name__ == "__main__":
    root = [1, 2, 3]
    tree = TreeNode(root)
    print(Solution().isSymmetric(tree))

    root = [1, 2, 2, 3, 4, 4, 3]
    tree = TreeNode(root)
    print(Solution().isSymmetric(tree))

    root = [1, 2, 2, None, 3, None, 3]
    tree = TreeNode(root)
    print(Solution().isSymmetric(tree))
