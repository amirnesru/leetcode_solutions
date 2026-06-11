class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right :
            if nums[left] < target and nums[right] > target :
                left+=1
                right-=1
            elif nums[left] >= target   :
                return left
            elif nums[right] < target  :
                return right + 1 
            elif nums[right] == target  :
                return right     
        return left
                
