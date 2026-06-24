class NumArray:

    def __init__(self, nums):
        self.arr = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.arr[i + 1] = self.arr[i] + nums[i]

    def sumRange(self, left, right):
        return self.arr[right + 1] - self.arr[left]