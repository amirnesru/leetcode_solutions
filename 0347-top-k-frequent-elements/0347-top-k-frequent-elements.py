from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       c = Counter(nums)
       keys_only=[key for key, count in c.most_common(k)]
       return keys_only  
            

        