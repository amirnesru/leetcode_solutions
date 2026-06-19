class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        d =  defaultdict(int)
        for i in range (len(nums)) :
            d[nums[i]]+=1
            if d[0] == 2 :
                while nums[left] == 1 :
                    left+=1
                d[0]-=1
                left +=1
            ans = max(ans , i - left)    
        return ans 