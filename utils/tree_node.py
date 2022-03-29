from typing import (
    List,
    Optional,
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

    def is_symmetric_trees(self, root1, root2) -> bool:
        if root1 and root2:
            return (
                root1.val == root2.val
                and self.is_symmetric_trees(root1.left, root2.right)
                and self.is_symmetric_trees(root1.right, root2.left)
            )
        if root1 is None and root2 is None:
            return True
        return False


def merge_trees(root1, root2) -> Optional:
    """Sums the current node and all nodes below recursively for the received roots."""
    result_node = TreeNode()
    if root1 is not None and root2 is not None:
        result_node.val = root1.val + root2.val
        result_node.left = merge_trees(root1.left, root2.left)
        result_node.right = merge_trees(root1.right, root2.right)
    elif root1 is not None and root2 is None:
        result_node = root1
    elif root1 is None and root2 is not None:
        result_node = root2
    elif root1 is None and root2 is None:
        return
    return result_node
