class Solution:
    def findMedian(self, nums):
        l = len(nums)
        if (l == 0):
            return None
        elif(l == 1):
            return nums[0]
        elif(l % 2 == 1):
            return nums[l // 2]
        else:
            return (nums[l // 2] + nums[l // 2 - 1]) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if(l1 == 0 and l2 == 0):
            return None
        elif(l1 == 0):
            return self.findMedian(nums2)
        elif(l2 == 0):
            return self.findMedian(nums1)

        flag2 = (l1 + l2) % 2
        nm = (l1 + l2) // 2 + 1

        nl = 0
        li1 = 0
        li2 = 0

        while(li1 < l1 or li2 < l2):
            if(li1 < l1 and li2 < l2):
                if(nums1[li1] <= nums2[li2]):
                    tmp = nums1[li1]
                    li1 += 1
                else:
                    tmp = nums2[li2]
                    li2 += 1
            elif(li1 < l1):
                tmp = nums1[li1]
                li1 += 1
            elif(li2 < l2):
                tmp = nums2[li2]
                li2 += 1

            nl += 1

            if(nl == nm):
                if(flag2 == 0):
                    tmp = (ret0 + tmp) / 2
                return tmp
            else:
                ret0 = tmp

        return None
