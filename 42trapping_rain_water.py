class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        l, r = 1, len(height) - 2
        lmax, rmax = height[0], height[-1]
        res = 0
        while l <= r:
            if lmax <= rmax:
                if height[l] < lmax:
                    res += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    res += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return res


"""
class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        lo, hi = 0, len(height) - 1
        result = 0
        left_max = right_max = 0

        while lo <= hi:
            if height[lo] < height[hi]:
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    result += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    result += right_max - height[hi]
                hi -= 1

        return result
"""
