from typing import (
    List,
    Union,
)


class TreeNode:
    """Tree of Nodes of a binary tree."""

    # original method signature on leetcode
    # def __init__(self, val=0, left=None, right=None):
    def __init__(self, val: Union[List[int], int] = 0, left=None, right=None, index=0):
        """Constructor for TreeNode."""
        if isinstance(val, List):
            self.val = val[index]
            if 2 * index + 1 < len(val) and val[2 * index + 1] is not None:
                self.left = TreeNode(val, index=2 * index + 1)
            else:
                self.left = left
            if 2 * index + 2 < len(val) and val[2 * index + 2] is not None:
                self.right = TreeNode(val, index=2 * index + 2)
            else:
                self.right = right
        elif isinstance(val, int):
            self.val = val
            self.left = left
            self.right = right
        else:
            raise TypeError(
                f"val should be int or a list of ints, received {type(val)}"
            )

    def _is_symmetric_trees(self, root1, root2) -> bool:
        if root1 and root2:
            return (
                root1.val == root2.val
                and self._is_symmetric_trees(root1.left, root2.right)
                and self._is_symmetric_trees(root1.right, root2.left)
            )
        if root1 is None and root2 is None:
            return True
        return False
