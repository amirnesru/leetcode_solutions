class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        max_len = 0
        while right < len(nums):
            if nums[right] == 0:    
                count+=1 
            if count > 1:
                while count > 1 :
                    if nums[left] == 0:
                        count -=1
                    left +=1
                    
            right+=1        
            max_len = max(max_len,right-left-1)  
               
           
                  
        return max_len            

