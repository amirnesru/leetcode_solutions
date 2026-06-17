class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        while True :
            n=list(str(n))
            count=0
            for i in range (len(n)):
                  count+=int(n[i])*int(n[i])
            n= count
            if n == 1:
                return True 
            if n in d :
                return False
            else :
                d[n]=1   

