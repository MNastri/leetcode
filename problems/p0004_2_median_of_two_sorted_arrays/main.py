from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lngt = len(nums1) + len(nums2)
        if lngt % 2 == 1:
            return self.get_kth_element(nums1, nums2, lngt // 2)
        else:
            left_of_median = self.get_kth_element(nums1, nums2, lngt // 2 - 1)
            right_of_median = self.get_kth_element(nums1, nums2, lngt // 2)
            return (left_of_median + right_of_median) / 2.0

    def get_kth_element(self, arr_a, arr_b, pos, slc_a=None, slc_b=None):
        """Gets the kth element of the array if arr_a and arr_b were to be merged.
        Assumes that arr_a and arr_b are sorted.
        Slices are used to recurse over the arrays without making copies or
        changing the arrays.

        Every call in this function is O(1).
        Every time this function is called the space is reduced by half.
        The function stops after all elements of the smallest array have been exausted.
         - time complexity: O(log(min(m,n)))
         - space complexity: O(1)
        """
        if slc_a is None and slc_b is None:
            # set the slices for the arrays
            slc_a = (0, len(arr_a))
            slc_b = (0, len(arr_b))
        if slc_a[0] == slc_a[1]:
            # arr_a is empty, median is in arr_b
            return arr_b[slc_b[0] + pos]
        if slc_b[0] == slc_b[1]:
            # arr_b is empty, median is in arr_a
            return arr_a[slc_a[0] + pos]
        # get the indexes for the medians
        idx_med_a = (slc_a[1] - slc_a[0]) // 2
        idx_med_b = (slc_b[1] - slc_b[0]) // 2
        # get the medians
        med_a = arr_a[slc_a[0]+idx_med_a]
        med_b = arr_b[slc_b[0]+idx_med_b]
        if idx_med_a + idx_med_b < pos:
            # the median is after the combined indexes of the medians of arr_a and arr_b
            if med_b < med_a:
                # arr_a median is bigger than arr_b median, the median can't be
                # in the first half of arr_b
                start = slc_b[0] + idx_med_b + 1
                stop = slc_b[1]
                slc_b = (start, stop)
                pos = pos - idx_med_b - 1
                return self.get_kth_element(arr_a, arr_b, pos, slc_a, slc_b)
            else:
                # arr_b median is bigger than arr_a median, the median can't be
                # in the first half of arr_a
                start = slc_a[0] + idx_med_a + 1
                stop = slc_a[1]
                slc_a = (start, stop)
                pos = pos - idx_med_a - 1
                return self.get_kth_element(arr_a, arr_b, pos, slc_a, slc_b)
        else:
            # the median is before the combined indexes of the medians of arr_a
            # and arr_b
            if med_b < med_a:
                # arr_a median is bigger than arr_b median, the median can't be
                # in the second half of arr_a
                start = slc_a[0]
                stop = slc_a[0] + idx_med_a
                slc_a = (start, stop)
                return self.get_kth_element(arr_a, arr_b, pos, slc_a, slc_b)
            else:
                # arr_b median is bigger than arr_a median, the median can't be
                # in the second half of arr_b
                start = slc_b[0]
                stop = slc_b[0] + idx_med_b
                slc_b = (start, stop)
                return self.get_kth_element(arr_a, arr_b, pos, slc_a, slc_b)


if __name__ == "__main__":
    arr1 = [1, 3]
    arr2 = [2]
    print(2)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
    arr1 = [1, 2]
    arr2 = [3, 4]
    print(2.5)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
    arr1 = [1, 2]
    arr2 = [3, 4, 5, 6]
    print(3.5)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
    arr1 = [1, 6]
    arr2 = [2, 3, 4, 5]
    print(3.5)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
    arr1 = [5, 6]
    arr2 = [1, 2, 3, 4]
    print(3.5)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
    arr1 = [1, 2, 2]
    arr2 = [1, 2, 3]
    print(2)
    print(Solution().findMedianSortedArrays(nums1=arr1, nums2=arr2))
