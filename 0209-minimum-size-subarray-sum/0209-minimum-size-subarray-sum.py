class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0 
        left = 0
        ans = float('inf')
        for i in range (len(nums)):
            sum+= nums[i]
            while sum >= target:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1
            
        return 0 if ans == float('inf') else ans