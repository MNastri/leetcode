# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
from typing import List

NUMS = [2, 7, 11, 15]
TARGET = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_hash = dict()
        for index, number in enumerate(nums):
            if number in complement_hash:
                index2 = complement_hash[number]
                return [index, index2]
            complement = target - number
            complement_hash[complement] = index
        return []

    def brute_force_two_sum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums[:-1]):
            for index2, number2 in enumerate(nums[index+1:], start=index+1):
                if nums[index] + nums[index2] == target:
                    return [index, index2]


def test( targets=None, numbs: List[int]=NUMS):
    print('Array usado %s' % numbs)
    a = Solution()
    if targets != None:
        print('meu target é: %s. resposta %s' % (targets, a.twoSum(nums=numbs, target=targets)))
        return
    for several_targets in range(0, 31):
        print('meu target é: %s. resposta %s' % (several_targets, a.twoSum(nums=numbs, target=several_targets)))


def main_loop():
    test()
    test(9, [2, 7, 11, 15])
    test(6, [3, 2, 4])
    test(6, [3, 3])


if __name__ == '__main__':
    main_loop()
