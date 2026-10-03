class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = [0]
        answer = [-1] * len(nums2)
        for i in range (1,len(nums2)):
                while len(stack) > 0 and  nums2[i] > nums2 [ stack [-1]]  :
                    answer[stack[-1]] = nums2[i]
                    stack.pop()
                stack.append(i)
        arr = []
        for i in nums1 :
            arr.append (nums2.index(i))
        ans = []
        for i in arr:
            ans.append(answer[i])
        return ans        
