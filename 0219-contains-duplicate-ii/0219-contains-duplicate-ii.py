class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       left = 0
       d = defaultdict(int)
       for i in range (len(nums)) :
            d[nums[i]]+=1
            if i > k :
                d[nums[left]]-=1
                left+=1
            if d[nums[i]] == 2:
                return True
            
       return False
    
        