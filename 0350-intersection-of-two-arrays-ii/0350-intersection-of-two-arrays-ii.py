class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       num1=Counter(nums1)
       num2=Counter(nums2)
       arr=[]      
       for i in num1:
            if i in num2:
                x=min(num1[i],num2[i])
                arr.extend(x*[i])
       return arr         
            