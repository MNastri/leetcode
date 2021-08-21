"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

Constraints:
-- 1 <= s.length <= 10**4
-- s consists of parentheses only '()[]{}'.
"""

from typing import List


class Solution:
    """ Solução do problema. Não precisa inicializar a classe"""
    def is_valid(self, ss: str) -> bool:
        """
        Retorne se a string tem abertura e fechamento de parenteses correta.
        :param ss: string contendo apenas sinais de parenteses.
        :return:
        """
        stack = []
        print(f'({stack})', end='. ')
        return False


def test(input_strs: str) -> None:
    """ Teste a string na solução."""
    print('\nInput: %s' % input_strs, end='. ')
    a = Solution()
    print('Output: %s' % a.is_valid(input_strs), end='. ')


def main_loop():
    test("()")                          # output:True
    test("()[]{}")                      # output:True
    test("(]")                          # output:False
    test("([)]")                        # output:False
    test("{[]}")                        # output:True


if __name__ == '__main__':
    main_loop()
