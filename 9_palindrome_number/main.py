# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while
# 123 is not.
#
# Example 1:
# Input: x = 121
# Output: true
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Example 4:
# Input: x = -101
# Output: false
#
# Constraints:
# -2^31 <= x <= 2^31 - 1

from typing import List


class Solution:
    def isPalindrome(self, xx: int) -> bool:
        rev = int(str(abs(xx))[::-1])
        return False if xx < 0 else False if rev.bit_length() > 31 or xx != rev else True

        # ideia geral: transformar em str e depois inverter os caracteres.

        # remover sinal negativo
        # transformar em string
        # inverter string
        # transformar em int
        # verificar se tem erro com tamanho do int
        # verificar se numero era negativo
        # verificar se é palindromo


def test(input_int):
    # FUNCIONOU DE PRIMEIRA ENTÃO NEM CRIEI TESTES
    # DEIXEI TESTES ANTIGOS COMO REFERÊNCIA

    # print('\n\nInput %s' % input_int, end='. ')
    # a = Solution()
    # print('Output %s' % a.reverse(input_int), end='. ')

    # print('\n\nInput %s' % input_int, end='. ')
    # a = Solution()
    # print('Output %s' % a.reverse_str(input_int), end='. ')
    return


def main_loop():
    # FUNCIONOU DE PRIMEIRA ENTÃO NEM CRIEI TESTES
    # DEIXEI TESTES ANTIGOS COMO REFERÊNCIA

    # test(123)
    # test(-123)
    # test(120)
    # test(-120)
    # test(0)
    # test(1_534_236_469)
    test(-1)


if __name__ == '__main__':
    main_loop()
