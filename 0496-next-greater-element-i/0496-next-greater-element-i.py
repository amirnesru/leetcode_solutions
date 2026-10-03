class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        answer = {}

        for num in nums2:

            while stack and num > stack[-1]:
                answer[stack[-1]] = num
                stack.pop()

            stack.append(num)

        while stack:
            answer[stack[-1]] = -1
            stack.pop()

        ans = []

        for num in nums1:
            ans.append(answer[num])

        return ans