class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=nums.count(0)
        y=nums.count(1)
        for i in range(x):
            nums[i]=0
        for i in range(y):
            nums[i+x]=1    
        for i in range (len(nums)-(x+y)):
            nums[i+x+y]=2
        return (nums)   

        