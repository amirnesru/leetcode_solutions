class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2+1
        ans = 0
        while low <= high:
            mid =  (low+high)//2
            print(mid)
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans-1            
