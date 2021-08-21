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
        :param ss: string contendo apenas sinais de parenteses dentre os caracteres '()[]{}'.
        :return:
        """
        open_parenth = '([{'
        close_parenth = ')]}'
        dict_open_parenth = dict(zip(open_parenth, close_parenth))
        # print(f'__{dict_parentheses}__', end='. ')

        stack_open_parenth = [ss[0]]
        # print(f'__{stack_open_parenth}__', end='. ')
        # print(f'__{ss[1:]}__', end='. ')
        if ss[0] in close_parenth:
            return False
        for character in ss[1:]:
            # print(f'__{character}__', end='. ')
            if character in open_parenth:
                stack_open_parenth.append(character)
                continue
            else:
                if 0 == len(stack_open_parenth):
                    return False
            if dict_open_parenth[stack_open_parenth.pop()] != character:
                return False
        # print(f'__{stack_open_parenth}__', end='. ')
        return True if 0 == len(stack_open_parenth) else False


def test(input_strs: str) -> None:
    """ Teste a string na solução."""
    print('\nInput:"%s"' % input_strs, end='. ')
    a = Solution()
    print('Output:%s' % a.is_valid(input_strs), end='. ')


def main_loop():
    test("()")                          # output:True
    test("()[]{}")                      # output:True
    test("(]")                          # output:False
    test("([)]")                        # output:False
    test("{[]}")                        # output:True
    print('\n')
    test("{")                           # output:False
    test("{[(")                         # output:False
    test("]")                           # output:False
    test(")]}")                         # output:False
    test("(){}}{")                      # output:False
    test("[])")                         # output:False


if __name__ == '__main__':
    main_loop()
