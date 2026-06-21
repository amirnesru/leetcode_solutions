class Solution:
    def partitionLabels(self, s: str):
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, d[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res