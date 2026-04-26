class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            l = i
            while l > 0 and heights[l] > heights[l-1]:
                names[l],names[l-1]=names[l-1],names[l]  
                heights[l],heights[l-1]=heights[l-1],heights[l]
                l-=1
        return names
