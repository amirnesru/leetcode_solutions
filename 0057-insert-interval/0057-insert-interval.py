from collections import Counter
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr=[]
        for i in intervals:
           if i[1] < newInterval[0]:
            arr.append(i)
           elif i[0]> newInterval[1]:
            arr.append(i)
           else:
            newInterval[0] = min(newInterval[0], i[0])
            newInterval[1] = max(newInterval[1], i[1])
        arr.append(newInterval)
          
       
        return sorted(arr)


