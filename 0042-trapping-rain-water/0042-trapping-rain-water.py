class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        lmax = 0
        rmax = 0
        count = 0

        while left < right:
            if height[left] < height[right]:
                lmax = max(lmax, height[left])
                count += lmax - height[left]
                left += 1
            else:
                rmax = max(rmax, height[right])
                count += rmax - height[right]
                right -= 1

        return count