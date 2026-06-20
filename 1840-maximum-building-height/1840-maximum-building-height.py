class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()

        # left -> right fix
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0])
            )

        # right -> left fix
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0])
            )

        ans = 0

        for i in range(1, len(restrictions)):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            ans = max(ans, (h1 + h2 + (x2 - x1)) // 2)

        return ans