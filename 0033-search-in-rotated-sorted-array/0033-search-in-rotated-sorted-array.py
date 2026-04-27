class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        reight=len(nums)-1
        for i in range (len(nums)//2+1):
            if nums[left]!= target and nums [reight] != target:
                left+=1
                reight-=1 
            
            elif  nums[left]== target or nums [reight] == target:  
                return left if nums[left]==target else  reight 
        else :
            return -1    