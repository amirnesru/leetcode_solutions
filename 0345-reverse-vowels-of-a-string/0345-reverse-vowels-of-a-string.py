class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0 
        right = len(s)-1
        s=list(s)

        while left < right :
            if s[left] not in ['A','E','I','O','U','a','e','i','o','u']:
                left+=1
            elif s[right] not in ['A','E','I','O','U','a','e','i','o','u'] :
                right -= 1
            else:
                s[left],s[right] = s[right], s[left]
                left += 1
                right -=1
        res=""        
        for i in s:
            res+=i
        return res    