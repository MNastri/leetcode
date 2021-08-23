"""
https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes
of the first two lists.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
-- The number of nodes in both lists is in the range [0, 50].
-- -100 <= Node.val <= 100
-- Both l1 and l2 are sorted in non-decreasing order.
"""

from typing import List, Optional


class ListNode:
    """ Uma lista de nodos linkada.

    representação
    [1,2,3] = 1->2->3
    """
    def __init__(self, val=0, nxt=None):
        self.value = val
        self.next = nxt
    def __str__(self):
        return str(self.value)

class Solution:
    """ Solução do problema. Não precisa inicializar a classe"""
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param l1:
        :param l2:
        :return:
        """
        return []

def test(ln1: ListNode, ln2: ListNode) -> None:
    """ Teste o input na solução."""
    print(f'\nInput:[{ln1}],[{ln2}', end='. ')
    a = Solution()
    print(f'Output:{a.mergeTwoLists(ln1, ln2)}', end='. ')


def main_loop():
    # testes com listas
    test([1,2,4], [1,3,4])
    test([],[])
    test([],[0])

    # implementar testes com ListNode que ainda não tenho certeza de como fazer
    # ln1 = ListNode([1,2,4])
    # ln2 = ListNode([1,3,4])
    # test(ln1, ln2)
    #
    # ln1 = ListNode([])
    # ln2 = ListNode([])
    # test(ln1, ln2)
    #
    # ln1 = ListNode([])
    # ln2 = ListNode([0])
    # test(ln1, ln2)


if __name__ == '__main__':
    main_loop()
