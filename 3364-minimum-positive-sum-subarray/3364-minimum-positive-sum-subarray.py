class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')
        n = len(nums)
        for i in range(l, r + 1):
            current_sum = sum(nums[:i])
            if current_sum > 0:
                ans = min(ans, current_sum)
                
            for j in range(i, n):
                current_sum = current_sum - nums[j - i] + nums[j]
                if current_sum > 0:
                    ans = min(ans, current_sum)
                    
        return ans if ans != float('inf') else -1
