from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        balanced = n // 4
        count = Counter(s)
        left = 0
        ans = n
         
        if all(count[char] <=  balanced for char in 'QWER'):
            return 0

        for right in range(n):
            count[s[right]] -= 1

            while left <= right and all(count[ch] <= balanced for ch in "QWER"):
                ans = min(ans, right - left + 1)

                count[s[left]] += 1
                left += 1

        return ans