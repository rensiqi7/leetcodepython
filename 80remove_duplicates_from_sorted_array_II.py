class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        end = len(nums)
        start = 1
        fstmem = nums[0]
        sndmem = None
        while start < end:
            if nums[start] == fstmem:
                if nums[start] == sndmem:
                    del nums[start]
                    end -= 1
                else:
                    sndmem = nums[start]
                    start += 1
            else:
                fstmem = nums[start]
                start += 1
        return len(nums)

        """
        if not nums:
            return 0

        last, i, same = 0, 1, False
        while i < len(nums):
            if nums[last] != nums[i] or not same:
                same = nums[last] == nums[i]
                last += 1
                nums[last] = nums[i]
            i += 1

        return last + 1
        """
