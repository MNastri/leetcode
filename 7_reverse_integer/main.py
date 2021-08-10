# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21
#
# Example 4:
# Input: x = 0
# Output: 0
#
# Constraints:
# -2^31 <= x <= 2^31 - 1

from typing import List

XX = 123


class Solution:
    def reverse(self, xx: int) -> int:
        reversed_number = 0
        was_negative = False
        while xx != 0:
            if xx < 0:
                xx *= -1
                was_negative = True
            reversed_number *= 10
            quotient, remainder = divmod(xx, 10)
            xx = quotient
            reversed_number += remainder
            # print('xx:%s' % xx, end=", ")
            # print('rev:%s' % reversed_number)
            if xx == 0:
                break
        if was_negative:
            reversed_number *= -1
        if reversed_number > 2_147_483_647 or reversed_number < -2_147_483_648:
            return 0
        return reversed_number

    def reverse_str(self, xx: int) -> int:
        was_negative = True if xx < 0 else False
        # print(str(xx)[1:][::-1], ' <-> ', str(xx)[::-1], end='. ')
        reversed_str = str(xx)[1:][::-1] if was_negative else str(xx)[::-1]
        reversed_integer = -int(reversed_str) if was_negative else int(reversed_str)
        if reversed_integer > 2_147_483_647 or reversed_integer < -2_147_483_648:
            return 0
        return reversed_integer

        # ideia geral: transformar em str e depois inverter os caracteres.

        # remover sinal negativo, se houver
        # transformar em string
        # inverter string
        # devolver sinal negativo, se havia
        # verificar se tem erro com tamanho do int
        #   lidar com erros
        # verificar se  começa com um ou mais zeros
        #   lidar com zeros
        # transformar em int
        # retornar numero invertido


def test(input_int):
    # print('\n\nInput %s' % input_int, end='. ')
    # a = Solution()
    # print('Output %s' % a.reverse(input_int), end='. ')

    print('\n\nInput %s' % input_int, end='. ')
    a = Solution()
    print('Output %s' % a.reverse_str(input_int), end='. ')
    return


def main_loop():
    test(123)
    test(-123)
    test(120)
    test(-120)
    test(0)
    test(1_534_236_469)
    test(-1)


if __name__ == '__main__':
    main_loop()
