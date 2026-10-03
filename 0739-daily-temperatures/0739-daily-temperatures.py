class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = [0]
        answer = [0] * len( temperatures)
        for i in range (1,len( temperatures)):
                while len(stack) > 0 and   temperatures[i] >  temperatures [ stack [-1]]  :

                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                
                stack.append(i)
        return answer
        
            