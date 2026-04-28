class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans=0
        for i in mat:
            if i.count(1) != 1 :
                continue 
            else :
                x=i.index(1)
                count=0
                for j in range (len(mat)):
                    if mat[j][x]==1:
                        count+=1  
                if count ==1:
                    ans+=1
        return ans        