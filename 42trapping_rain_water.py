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
