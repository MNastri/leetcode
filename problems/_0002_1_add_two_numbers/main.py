from itertools import combinations_with_replacement

# Definition for singly-linked list.
from typing import Optional

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
DIGIT_COMBINATIONS = combinations_with_replacement(DIGITS, r=2)
PAIRS = [p for p in DIGIT_COMBINATIONS]
NUMBERS = [nn for nn in range(0, 100_001)]
NUMBER_PAIRS = combinations_with_replacement(NUMBERS, r=2)


class ListNode:
    def __init__(self, val=0, next=None):
        if val not in DIGITS and next is None:
            self.val = int(str(val)[-1])
            self.next = ListNode(val=int(str(val)[:-1]), next=None)
        elif val not in DIGITS and next is not None:
            raise KeyError("inicialização incorreta do nodo")
        else:
            self.val = val
            self.next = next

    def get_int_representation(self):
        str_representation = ""
        current_node = self
        while current_node is not None:
            str_representation = str(current_node.val) + str_representation
            current_node = current_node.next
        return int(str_representation)

    def __repr__(self):
        return f"{self.get_int_representation():,}"


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        _carry, _remai = divmod(l1.val + l2.val, 10)
        result_node = ListNode(val=_remai)
        iter_node = result_node
        l1 = l1.next
        l2 = l2.next
        while l1 is not None or l2 is not None:
            if _carry == 0 and l1 and not l2:
                iter_node.next = l1
                return result_node
            elif _carry == 0 and l2 and not l1:
                iter_node.next = l2
                return result_node
            val_1 = 0 if l1 is None else l1.val
            val_2 = 0 if l2 is None else l2.val
            sum = val_1 + val_2 + _carry
            _carry, _remai = divmod(sum, 10)
            iter_node.next = ListNode(val=_remai)
            iter_node = iter_node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if _carry != 0:
            iter_node.next = ListNode(val=_carry)
        return result_node


def big_test():
    for a, b in NUMBER_PAIRS:
        nd_a = ListNode(val=a)
        nd_b = ListNode(val=b)
        val_a = nd_a.get_int_representation()
        val_b = nd_b.get_int_representation()
        sol = Solution().addTwoNumbers(nd_a, nd_b)
        assert sol.get_int_representation() == val_a + val_b
    print("big test ok.")


if __name__ == "__main__":
    big_test()
