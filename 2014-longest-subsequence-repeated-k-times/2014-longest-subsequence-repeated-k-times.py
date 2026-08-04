class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        d = Counter(s)
        passed = sorted([key for key, value in d.items() if value >= k], reverse=True )       
        result = ""
        arr = [""]
        while arr:
            curr = arr.pop(0)
            if len(curr) > len(result) or (len(curr) == len(result) and curr > result):
                result = curr
            for char in passed:
                nxt = curr + char
                target = nxt * k                
                i = 0
                for c in s:
                    if i < len(target) and c == target[i]:
                        i += 1
                
                if i == len(target):
                    arr.append(nxt)
        return result