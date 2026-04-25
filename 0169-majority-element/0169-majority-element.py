from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        a=len(nums)//2
        for i in count :
            if count[i]>a:
                return i
