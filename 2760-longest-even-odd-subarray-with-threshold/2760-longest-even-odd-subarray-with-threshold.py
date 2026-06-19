class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        left = 0 
        count = 0
        ans = 0
        while left < len(nums):
            if left+1 == len(nums) and nums[left] <= threshold and nums[left]%2 == 0:
                count+=1
                ans = max(ans,count)
                left+=1
            
            elif nums[left] % 2 == 0 and nums[left] <= threshold and nums[left+1] <= threshold and nums[left+1] % 2 !=  0 :
                count+=2
                ans = max(ans,count)
                left+=2 
            elif nums[left] % 2 == 0 and nums[left] <= threshold and nums[left+1] > threshold and nums[left+1] % 2 !=  0 :
                count+=1
                ans = max(ans,count)
                count = 0
                left+=2     
            else :
                if nums [left] % 2 == 0 and nums[left]<= threshold :
                     count += 1
                ans = max(ans,count)
                left +=1
                count=0   
        return ans 


        