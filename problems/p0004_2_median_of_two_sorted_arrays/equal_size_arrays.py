from typing import List

from problems.p0004_2_median_of_two_sorted_arrays.main import (
    get_lower_half_of,
    get_upper_half_of,
    get_array_median,
)


def median_of_arrays(array1: List[int], array2: List[int]) -> float:
    if len(array1) == len(array2) == 2:
        return (max([array1[0], array2[0]]) + min([array1[1], array2[1]])) / 2
    if len(array1) == len(array2) == 1:
        return (array1[0] + array2[0]) / 2
    if len(array1) == len(array2) == 0:
        raise TypeError("arrays should be non-empty")
    if len(array1) != len(array2):
        raise TypeError("arrays should have the same size")
    m1 = get_array_median(array1)
    m2 = get_array_median(array2)
    new_array1 = None
    new_array2 = None
    if m1 == m2:
        return m1
    if m1 < m2:
        # median(array1) <= median_of_arrays <= median(array2)
        # discard beginning of array1 and ending of array2
        new_array1 = get_upper_half_of(array=array1)
        new_array2 = get_lower_half_of(array=array2)
    elif m2 < m1:
        # median(array2) <= median_of_arrays <= median(array1)
        # discard beginning of array2 and ending of array1
        new_array1 = get_lower_half_of(array=array1)
        new_array2 = get_upper_half_of(array=array2)
    return median_of_arrays(array1=new_array1, array2=new_array2)


if __name__ == "__main__":
    arr1 = [14, 36, 96]
    arr2 = [12, 26, 82]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    arr1 = [10, 14, 36, 96]
    arr2 = [0, 12, 26, 82]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)

    arr1 = [0, 0, 0, 0, 0, 0, 44, 78, 86]
    arr2 = [4, 21, 25, 35, 45, 74, 77, 93, 94]
    solution = get_array_median(sorted(arr1 + arr2))
    print(solution)
    func_solution = median_of_arrays(array1=arr1, array2=arr2)
    print(func_solution)
