class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left_g = 0
        left_s = 0
        s.sort()
        g.sort()
        count = 0
        if len(s) == 0 :
            return 0
        while left_g < len(g) and left_s < len(s):
            if s[left_s] >= g[left_g]:
                count += 1
                left_g += 1
                left_s += 1
            else:
                left_s += 1
        return count           


