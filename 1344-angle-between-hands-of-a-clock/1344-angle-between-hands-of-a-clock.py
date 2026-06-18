class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        value = abs((minutes * 6) - ((hour%12) * 30) - (minutes / 2) )
        return min(360-value , value)