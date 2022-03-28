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
