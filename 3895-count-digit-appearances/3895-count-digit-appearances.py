class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            if str(digit) in str(i):
                count+=str(i).count(str(digit))
        return count         
