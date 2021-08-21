"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
-- 1 <= strs.length <= 200
-- 0 <= strs[i].length <= 200
-- strs[i] consists of only lower-case English letters.
"""

from typing import List


class Solution:
    """ Solução do problema. Não precisa inicializar a classe"""
    def longest_common_prefix(self, strs: List[str]) -> str:
        # ideias:
        # salvar no string de retorno a primeira string dos inputs
        # para as strings do input que não sejam a primeira
        #   para os índices da string de retorno
        #       comparar a string de retorno, até o índice usado, com ...
        #       ...o prefixo, usando o mesmo índice, da string do input usado
        #           se ret e pref forem iguais, continue
        #           se ret e pref forem diferentes, retirar caracteres extras de ret
        # quando a string de retorno tiver tamanho zero, retornar ""
        if 0 == len(strs):
            return ''
        if 1 == len(strs):
            return strs[0]
        return_str: str = strs[0]

        for items in strs[1:]:
            for index in range(1, len(return_str)+1):
                # estranhamente return_str[0] = '', então tem que verificar a string a partir do índice 1
                print(f'({return_str[:index]}', end=',')
                print(f'{items[:index]})', end='.')
                if items[:index] != return_str[:index]:
                    return_str = return_str[:index-1]
                    print(f'=>{return_str}', end='.')
                    break
        return return_str


def test(input_strs: List[str]) -> None:
    """ Teste a string na solução."""
    print('\nInput %s' % input_strs, end='. ')
    a = Solution()
    print('Output "%s"' % a.longest_common_prefix(input_strs), end='. ')


def main_loop():
    test([])                            # output:""
    test(['testing'])                   # output:"testing"
    test(['a', 'ab', 'abc'])            # output:"a"
    test(['a', 'abc', 'ab'])            # output:"a"
    test(['ab', 'a', 'abc'])            # output:"a"
    test(['ab', 'abc', 'a'])            # output:"a"
    test(['abc', 'a', 'ab'])            # output:"a"
    test(['abc', 'ab', 'a'])            # output:"a"
    test(['flower', 'flow', 'flight'])  # output:"fl"
    test(['dog', 'racecar', 'car'])     # output:""


if __name__ == '__main__':
    main_loop()
