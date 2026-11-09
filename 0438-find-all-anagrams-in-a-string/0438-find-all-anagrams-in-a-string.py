from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        p_count = Counter(p)
        window = defaultdict(int)
        k = len(p)
        for i in range(len(s)):
            window[s[i]] += 1

            if i >= k:
                left = s[i - k]
                window[left] -= 1

                if window[left] == 0:
                    del window[left]

            if window == p_count:
                res.append(i - k + 1)

        return res