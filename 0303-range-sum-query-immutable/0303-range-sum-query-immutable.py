class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        arr = [0]*(len(self.nums)+1)
        for i in range (len(self.nums)):
            arr[i+1] = arr[i] + self.nums[i]
        return (arr[right+1]-arr[left])
        
    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)