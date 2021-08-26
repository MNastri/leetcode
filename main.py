"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the
first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
extra memory.

Custom Judge:

The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
Constraints:

0 <= nums.length <= 3 * 10**4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
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
