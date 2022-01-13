from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        count_valid_ints = 0
        for idx, number in enumerate(nums):
            if number == val:
                nums[idx] = float('inf')
                continue
            count_valid_ints += 1
        nums.sort()
        # nums[:] = [2, 2, float('inf'), float('inf')]  # in place change of elements
        # return 2
        # nums[:] = [0, 1, 4, 0, 3, float('inf'), float('inf'), float('inf')]  # in place change of elements
        # return 5
        return count_valid_ints


def judge_case(nums: List[int], val, k, expectedNums):
    solution = Solution()
    my_k = solution.removeElement(nums, val)
    assert my_k == k
    nums.sort()
    for idx, (solved_int, solution_int) in enumerate(zip(nums, expectedNums)):
        if idx < k:
            assert solved_int == solution_int


if __name__ == '__main__':
    judge_case([3, 2, 2, 3], 3, 2, [2, 2, float('inf'), float('inf')])
    judge_case([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 0, 1, 3, 4, float('inf'), float('inf'), float('inf')])

