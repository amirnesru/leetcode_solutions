class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        checker = skill[0]+skill[-1]
        left = 0
        right =(len(skill)-1)
        total = 0 
        while left < right :
            if skill[left]+skill[right] != checker:
           
                return -1
            else:
                total+=(skill[left]*skill[right])
                left+=1
                right-=1
        return total

       
                

