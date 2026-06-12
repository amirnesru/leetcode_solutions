class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currMax = sum(nums[:k])
        maximum = currMax
        left=0
        right=k
        for i in range (len(nums)-(k)):
            currMax+=nums[right]
            currMax-=nums[left]
            if currMax > maximum :
                maximum = currMax
            left+=1
            right+=1    

        return maximum/k
