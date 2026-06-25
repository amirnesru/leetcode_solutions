class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        res = 0

        for price in prices:
            res = max(res, price - minimum)
            minimum = min(minimum, price)

        return res