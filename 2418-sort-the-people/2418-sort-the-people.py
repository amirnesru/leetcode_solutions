class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=sorted(heights,reverse=True)
        abb=[]
        for i in  arr:
            x=heights.index(i)
            abb.append(names[x])
        return abb        

