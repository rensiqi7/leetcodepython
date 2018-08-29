class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1 = m - 1
        index2 = n - 1
        write_index = m + n - 1
        if n < 1:
            return
        while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[write_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[write_index] = nums2[index2]
                index2 -= 1
            write_index -= 1
        return
