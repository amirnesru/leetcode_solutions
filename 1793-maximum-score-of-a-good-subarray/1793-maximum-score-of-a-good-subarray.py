class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        n = len(nums)        
        curr_min = nums[k]
        max_val = curr_min
        
        while i > 0 or j < n - 1:
            if i == 0:
                j += 1
            elif j == n - 1:
                i -= 1
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1                
            curr_min = min(curr_min, nums[i], nums[j])
            max_val = max(max_val, curr_min * (j - i + 1))
            
        return max_val
