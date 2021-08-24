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
    """ Nodos para uma lista linkada."""
    def __init__(self, value=0, nxt=None):
        self.val = value
        self.next = nxt

    def print_val(self):
        items = []
        items.append(self.val)
        if self.next == None:
            return
        node = self.next
        while node:
            items.append(node.val)
            node = node.next
        print(f'{items}')


class Solution:
    """ Solução do problema. Não precisa inicializar a classe"""
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        :param l1:
        :param l2:
        :return:
        """
        tail = dummy = ListNode()
        # l1.print_val()
        # l2.print_val()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        # dummy.print_val()
        return dummy.next


def test(ln1: ListNode, ln2: ListNode) -> None:
    """ Teste o input na solução."""
    print(f'\nInput:{ln1},{ln2}', end='. ')
    a = Solution()
    print(f'Output:{a.merge_two_lists(ln1, ln2)}', end='. ')


def main_loop():
    # implementar testes com ListNode que ainda não tenho certeza de como fazer
    ln1 = ListNode(4)
    ln1 = ListNode(2, ln1)
    ln1 = ListNode(1, ln1)

    ln2 = ListNode(4)
    ln2 = ListNode(3, ln2)
    ln2 = ListNode(1, ln2)

    test(ln1, ln2)

    # ln1 = ListNode([1, 2, 4])
    # ln2 = ListNode([1, 3, 4])
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
