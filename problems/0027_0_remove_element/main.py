from typing import List


class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        count_valid_ints = 0
        for idx, number in enumerate(nums):
            if number == val:
                nums[idx] = float("inf")
                continue
            count_valid_ints += 1
        nums.sort()
        return count_valid_ints


def judge_case(nums: List[int], val: int, k: int, expected_nums: List[int]) -> None:
    my_k = Solution().remove_element(nums=nums, val=val)
    assert my_k == k
    nums.sort()
    for idx, (solved_int, solution_int) in enumerate(zip(nums, expected_nums)):
        if idx < k:
            assert solved_int == solution_int


if __name__ == "__main__":
    judge_case(
        nums=[3, 2, 2, 3],
        val=3,
        k=2,
        expected_nums=[2, 2, float("inf"), float("inf")],
    )
    judge_case(
        nums=[0, 1, 2, 2, 3, 0, 4, 2],
        val=2,
        k=5,
        expected_nums=[0, 0, 1, 3, 4, float("inf"), float("inf"), float("inf")],
    )
