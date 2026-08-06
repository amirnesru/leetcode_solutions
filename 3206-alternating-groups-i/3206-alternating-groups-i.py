class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        left = 0
        right = left+2
        count = 0
        while right  < len(colors):
            if colors[left] != colors[left+1] and colors[right] != colors[left+1] :
                count+=1
            left +=1
            right+=1
        if colors[0] != colors[-1] :
            if colors[0] != colors[1]:
                count+=1    
            if colors[-1] != colors[-2]:
                count+=1
        return count