class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        print(arr)

        stack = []
        ans = ""

        for i in arr:
            if i == "..": 
                if stack:
                    stack.pop()

            elif i != "." and i:
                stack.append(i)

        res = "/" + "/".join(stack)

        return res


