class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)
        for j in range (n-3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue    
            for i in range(j+1,n - 2):
                if nums[j] + nums[i+1] + nums[i+2] + nums[i] > target:
                    break
                
                if nums[j] +nums[i] + nums[-2] + nums[-1] < target:
                    continue
                if i > j+1 and nums[i] == nums[i - 1]:
                    continue

                left, right = i + 1, n - 1

                while left < right:
                    total = nums[j]+nums[i] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[j],nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
        return res