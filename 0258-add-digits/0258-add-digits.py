class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        
        while len(s) > 1:
            a = 0
            for ch in s:
                a += int(ch)
            s = str(a)
        
        return int(s)