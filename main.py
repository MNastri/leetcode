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
        if 0 == len(strs):
            return ""
        if 1 == len(strs):
            return strs[0]
        return_str: str = strs[0]

        # for first_item in strs:
        #     for second_item in strs[1:]:
        #         print(f'len(return_strs)=={len(return_str)}')
        #         if 0 == len(return_str):
        #             return ""
        #         return_str = return_str[:1]
        #         pass
        # comparar itens dois a dois
        # nos itens, comparar letra a letra?
        # já tenho uma string de retorno, como comparar string com string?
        # como reduzir o tamanho da string de retorno caso não haja o prefixo nas duas strings?
        # quando a string de retorno tiver tamanho zero, retornar ""
        return return_str


def test(input_strs: List[str]) -> None:
    """ Teste a string na solução."""
    print('\nInput %s' % input_strs, end='. ')
    a = Solution()
    print('Output "%s"' % a.longest_common_prefix(input_strs), end='. ')


def main_loop():
    test([])                            #output:""
    test(['testing'])                   #output:"testing"
    test(['flower', 'flow', 'flight'])  #output:"fl"
    test(['dog', 'racecar', 'car'])     #output:""



if __name__ == '__main__':
    main_loop()
