class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[target-nums[i]] = i
            else: 
                return [a[nums[i]], i]