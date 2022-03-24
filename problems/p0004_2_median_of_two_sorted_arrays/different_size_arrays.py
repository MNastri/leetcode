from typing import List

from problems.p0004_2_median_of_two_sorted_arrays.equal_size_arrays import (
    median_of_arrays as median_of_arrays_same_size,
)
from problems.p0004_2_median_of_two_sorted_arrays.main import (
    get_array_median,
    get_arrays_between_medians,
    left_of_median,
    right_of_median,
)


def median_of_arrays(array1: List[int], array2: List[int]) -> float:
    if len(array1) != len(array2):
        tmp_array1 = array1 if len(array1) < len(array2) else array2
        tmp_array2 = array2 if len(array1) < len(array2) else array1
        size = len(tmp_array1) + len(tmp_array2)
        el = tmp_array1[0]
        left = left_of_median(tmp_array2)
        right = right_of_median(tmp_array2)
        if len(tmp_array1) == 1 and size % 2 == 0:
            med = get_array_median(tmp_array2)
            if el < left or el == left:
                return (left + med) / 2
            if el < med:
                return (el + med) / 2
            if el == med:
                return el
            if el < right:
                return (el + med) / 2
            if el == right or right < el:
                return (med + right) / 2
        if len(tmp_array1) == 1 and size % 2 == 1:
            if el < left:
                return left
            if el == left:
                return el
            if el < right:
                return el
            if el == right:
                return el
            if right < el:
                return right
        if len(tmp_array1) != 1:
            if len(array1) == 0 or len(array2) == 0:
                raise TypeError("arrays should be non-empty")
        new_array1, new_array2 = get_arrays_between_medians(array1, array2)
        return median_of_arrays(array1=new_array1, array2=new_array2)
    elif len(array1) == len(array2):
        return median_of_arrays_same_size(array1=array1, array2=array2)


if __name__ == "__main__":
    # arr1 = [18, 24, 27, 45, 46, 62, 76]
    # arr2 = [3, 5, 8, 9, 11, 20, 24, 32, 37, 40, 48, 58, 62, 69, 77, 84, 92, 98, 99]

    # m1==m2, odd size
    arr1 = [17]
    arr2 = [2, 32]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    # m1<m2, odd size
    arr1 = [18]
    arr2 = [3, 34]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    # m2<m1, odd size
    arr1 = [19]
    arr2 = [3, 32]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)
    #############
    # m1==m2, even size
    arr1 = [17]
    arr2 = [2, 17, 70]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    # m1<m2, even size
    arr1 = [18]
    arr2 = [3, 34, 70]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    # m2<m1, even size
    arr1 = [19]
    arr2 = [3, 15, 70]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)
