from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        slow = 0
        fast = 0
        ans = 0
        maxi = deque()
        mini = deque()

        while fast < len(nums):
            while maxi and nums[maxi[-1]] < nums[fast]:
                maxi.pop()
            maxi.append(fast)

            while mini and nums[mini[-1]] > nums[fast]:
                mini.pop()
            mini.append(fast)

            while nums[maxi[0]] - nums[mini[0]] > limit:
                if maxi[0] == slow:
                    maxi.popleft()
                if mini[0] == slow:
                    mini.popleft()
                slow += 1

            ans = max(ans, fast - slow + 1)
            fast += 1

        return ans