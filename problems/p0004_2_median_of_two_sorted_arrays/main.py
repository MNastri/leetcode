from typing import (
    List,
    Tuple,
)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


def left_of_median(array: List[int]) -> int:
    ll = len(array)
    if ll % 2 == 0:
        return array[int(ll / 2 - 1)]
    return array[int(ll / 2 - 3 / 2)]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(left_of_median(array=arr))
    arr = [0, 7, 39, 42, 70]
    print(left_of_median(array=arr))


def right_of_median(array: List[int]) -> int:
    ll = len(array)
    if ll % 2 == 0:
        return array[int(ll / 2)]
    return array[int(ll / 2 + 1)]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(right_of_median(array=arr))
    arr = [0, 7, 23, 39, 70]
    print(right_of_median(array=arr))


def get_array_median(array: List[int]) -> float:
    ll = len(array)
    if ll == 1:
        return array[0]
    if ll % 2 == 0:
        left = left_of_median(array=array)
        right = right_of_median(array=array)
        return (left + right) / 2
    return array[int((ll - 1) / 2)]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(get_array_median(array=arr))
    arr1 = [0, 7, 25, 39, 42]
    print(get_array_median(array=arr1))


def get_upper_half_of(array):
    ll = len(array)
    if ll == 1:
        return array
    if ll % 2 == 0:
        return array[int(ll / 2) :]
    return array[int(((ll - 1) / 2)) :]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(get_upper_half_of(array=arr))
    arr1 = [0, 7, 23, 39, 42]
    print(get_upper_half_of(array=arr1))


def get_lower_half_of(array):
    ll = len(array)
    if ll == 1:
        return array
    if ll % 2 == 0:
        return array[: int(ll / 2)]
    return array[: int((ll + 1) / 2)]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(get_lower_half_of(array=arr))
    arr1 = [0, 7, 23, 39, 42]
    print(get_lower_half_of(array=arr1))


def get_arrays_between_medians(
    array1: List[int], array2: List[int]
) -> Tuple[List[int], List[int]]:
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
    return new_array1, new_array2
