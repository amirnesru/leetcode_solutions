class Solution:
    def can(self, mid: int) -> bool:
        curr = 0
        count = 1

        for i in self.weights:
            if curr + i > mid:
                count += 1
                curr = i
            else:
                curr += i

        return count <= self.day

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        self.weights = weights
        self.day = days

        low = max(weights)
        high = sum(weights)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.can(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1

        return ans