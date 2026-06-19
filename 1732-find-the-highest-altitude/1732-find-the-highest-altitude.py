class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        count = 0 
        for i in range (len(gain)) :
            count += gain[i]
            max_alt = max(max_alt, count)
        return max_alt