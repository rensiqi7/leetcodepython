class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = nums1 + nums2
        combined.sort()
        count = len(combined)
        index = count // 2
        if count % 2 == 0:
            median = (combined[index - 1] + combined[index]) / 2
        elif count % 2 == 1:
            median = combined[index]
        return median
