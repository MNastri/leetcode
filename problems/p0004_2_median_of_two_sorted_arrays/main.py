from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


def median(array: List[int]) -> float:
    ll = len(array)
    if ll == 1:
        return array[0]
    if ll % 2 == 0:
        left_of_median = array[int(ll / 2 - 1)]
        right_of_median = array[int(ll / 2)]
        return (left_of_median + right_of_median) / 2
    return array[int((ll - 1) / 2)]


if __name__ == "__main__":
    arr = [0, 7, 39, 42]
    print(median(array=arr))
    arr1 = [0, 7, 23, 39, 42]
    print(median(array=arr1))


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


def merge_arrays(array1: List[int], array2: List[int]) -> List[int]:
    if len(array1) <= len(array2):
        tmp_arr0 = array1
        tmp_arr1 = array2
    elif len(array2) < len(array2):
        tmp_arr0 = array2
        tmp_arr1 = array1
    # pick first element of tmp_arr0
    # compare with median of tmp_arr1
    # LOOP1
    # LOOP
    # if smaller, get subarray up until median
    # if bigger , get subarray from median and on
    # compare element with the median of subarray
    # repeat until len of subarray == 2 (GOTO LOOP)
    #
    # if right_item < element, rebuild subarray and return it
    # elif left_item < element, rebuild subarray and return it
    # else left_item == righ_item, rebuild subarray and return it
    #
    # find index of element added into tmp_arr1
    # exclude from checking before this point in array by creating a new tmp_arr1
    # pick next element of tmp_arr0
    # compare with median of tmp_arr1
    # repeat until reaching end of tmp_arr0 (GOTO LOOP1)
    return tmp_arr1
