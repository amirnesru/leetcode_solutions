class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1=len(nums1)
        num2= len(nums2)
        x=(num1+num2) 
        arr=[]
        xx=0
        yy=0
        for _ in range(x//2 + 1):
            if yy == num2 or (xx < num1 and nums1[xx] < nums2[yy]):
                arr.append(nums1[xx])
                xx += 1
            else:
                arr.append(nums2[yy])
                yy += 1
                    
        return (arr[-1]+arr[-2])/2 if x%2==0 else arr[-1]