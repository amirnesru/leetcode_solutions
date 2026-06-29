class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        left2, right2 = 0, len(nums)-1
        result = -1
        result2 = -1
        while left <= right :
            mid = (left + right )//2

            if nums[mid] == target :
                result = mid
                right = mid - 1
            elif nums [mid] > target :
                right = mid - 1 
            else :
                left = mid + 1
        while left2 <= right2 :
            mid2 = (left2 + right2 )//2

            if nums[mid2] == target :
                result2 = mid2
                left2 = mid2 + 1
            elif  nums[mid2] < target:
                left2 = mid2 + 1   
            else :
                right2 = mid2 - 1
        return [result,result2]        