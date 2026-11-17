class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for i in arr:
            if stack and i == ".." :
                stack.pop()
            elif i == "." or i == "":
                continue
            else:
                if i == "..":
                    continue
                stack.append(i)
        print(stack)        
        stack = "/".join(stack)
        stack = "/"+stack         
        return stack   

