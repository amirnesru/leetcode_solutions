class Solution:
    def reverseWords(self, s: str) -> str:
        left=0
        right=left+1
        result=""
        while right < len(s):
            if s[right] != " ":
                right+=1
            else:
                result=result+s[left:right][::-1]+s[right]
                left=right+1
                right+=1    
        result=result+s[left:][::-1]
        return result