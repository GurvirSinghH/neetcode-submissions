class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 1
        right = n - 2
        lmax = height[left-1]
        rmax = height[right + 1]
        max_water_trapped = 0
        while left <= right:
            if rmax <= lmax:
                max_water_trapped += max(0, rmax - height[right])
                rmax = max(rmax, height[right])
                right -= 1
            else:
                max_water_trapped += max(0, lmax - height[left])
                lmax = max(lmax, height[left])
                left += 1
        return max_water_trapped