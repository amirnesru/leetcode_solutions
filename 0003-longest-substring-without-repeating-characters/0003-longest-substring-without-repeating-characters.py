class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window= defaultdict(int)
        left = 0
        max_len = 0
        for i in range (len(s)):
            window[s[i]]+=1
            while window[s[i]] > 1 :
                window[s[left]]-=1
                if window[s[left]]==0 :
                    del window[s[left]]
                left+=1
            
            max_len = max(max_len, i-left+1)
        return  max_len

