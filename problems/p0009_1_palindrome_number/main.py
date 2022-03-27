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
    # def helper_palindrome(self, xx: int, count: int) -> bool:
    #     if count == 1:
    #         return True

    def is_palindrome(self, xx: int) -> bool:
        if xx < 0:
            return False
        if len('%i' % xx) == 1:
            return True
        if str(xx)[0] == str(xx)[-1]:
            if len('%i' % xx) == 2:
                return True
            new_xx_str = str(xx)[1:-1]
            if new_xx_str[0] == '0':
                lead_zeros = len(new_xx_str) - len(new_xx_str.lstrip('0'))
                if lead_zeros == len(new_xx_str):
                    return True
                trail_zeros = len(new_xx_str) - len(new_xx_str.rstrip('0'))
                if lead_zeros != trail_zeros:
                    return False
                new_xx_str = new_xx_str[lead_zeros:-trail_zeros]
            return self.is_palindrome(int(new_xx_str))
        return False

    def is_palindrome_str(self, xx: int) -> bool:
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


def test(input_int: int) -> None:
    # tenho que aprender a colocar testes que retornam True, False ou então um código de erro para indicar erro
    print('\nInput %i' % input_int, end='. ')
    a = Solution()
    print('Output %s' % a.is_palindrome(input_int), end='. ')


def main_loop():
    test(1_000_021)
    test(100_020_001)
    test(100_002_001)
    # testar os negativos
    for ii in range(-1, -1_000, -1):
        test(ii)
    # testar os não negativos
    for ii in range(1_000):
        test(ii)


if __name__ == '__main__':
    main_loop()
