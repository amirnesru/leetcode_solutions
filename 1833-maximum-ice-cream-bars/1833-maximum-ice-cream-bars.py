class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (max(costs) + 1)

        for cost in costs:
            count[cost] += 1

        ans = 0

        for cost in range(1, len(count)):
            if count[cost]:
                buy = min(count[cost], coins // cost)
                ans += buy
                coins -= buy * cost

        return ans