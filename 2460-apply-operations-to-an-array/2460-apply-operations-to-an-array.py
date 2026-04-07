class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        x=nums.count(0)       
        abb=[]
        acc=[0]*x
        for i in nums:
            if i!=0:
                abb.append(i)
        return abb+acc        
