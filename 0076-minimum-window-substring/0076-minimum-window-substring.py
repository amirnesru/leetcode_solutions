from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter(t)
        d = defaultdict(int)

        len_dic = len(dic)
        count = 0

        left = 0
        ans = (float("inf"), "")

        for right in range(len(s)):
            d[s[right]] += 1

            if s[right] in dic and d[s[right]] == dic[s[right]]:
                count += 1

            while count == len_dic:
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, s[left:right+1])

                d[s[left]] -= 1

                if s[left] in dic and d[s[left]] < dic[s[left]]:
                    count -= 1

                left += 1

        return ans[1]