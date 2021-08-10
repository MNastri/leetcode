# # Given an array of integers nums and an integer target,
# # return indices of the two numbers such that they add up to target.
# #
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# #
# # You can return the answer in any order.
# #
# # Example 1:
# #
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# #
# # Example 2:
# #
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]
# #
# # Example 3:
# #
# # Input: nums = [3,3], target = 6
# # Output: [0,1]
# #
# # Constraints:
# #
# # 2 <= nums.length <= 104
# # -109 <= nums[i] <= 109
# # -109 <= target <= 109
# # Only one valid answer exists.
# #
# # Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
#
# def find_solution(nums: List[int], target: int) -> List[int]:
#     for index, numero in enumerate(nums):
#         # for index2, numero2 in enumerate(nums, start=index+1):
#         for index2, numero2 in enumerate(nums[index+1:], start=index+1):
#             # print('[%s, %s] = (%s, %s)' % (index, index2, numero, numero2))
#             if nums[index] + nums[index2] == target:
#                 return [index, index2]
#         pass
#     pass
#
#
# NUMS = [2, 7, 11, 15]
# TARGET = 26
#
# if __name__ == '__main__':
#     a = find_solution(nums=NUMS, target=TARGET)
#     print(a)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):
            for index2, number2 in enumerate(nums[index+1:], start=index+1):
                if nums[index] + nums[index2] == target:
                    return [index, index2]
