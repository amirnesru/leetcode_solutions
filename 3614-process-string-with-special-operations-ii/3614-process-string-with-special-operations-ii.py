class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        n = len(s)

        # first pass: find final length
        for ch in s:
            if ch == "*":
                if length > 0:
                    length -= 1
            elif ch == "#":
                length *= 2
            elif ch == "%":
                pass
            else:
                length += 1

        if k >= length:
            return "."

        
        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch == "*":
                length += 1

            elif ch == "#":
                half = length // 2
                if k >= half:
                    k -= half
                length = half

            elif ch == "%":
                k = length - 1 - k

            else:
                if k == length - 1:
                    return ch
                length -= 1

        return "."