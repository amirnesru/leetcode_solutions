class Solution:
    def isValid(self, s: str) -> bool:
        brack = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        arr = []

        for ch in s:
            if ch in "([{":
                arr.append(ch)
            else:
                if not arr or arr.pop() != brack[ch]:
                    return False

        return len(arr) == 0

