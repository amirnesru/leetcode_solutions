class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        for i in range(m):
            ind = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == "*":
                    ind = j - 1
                elif boxGrid[i][j] == "#":
                    boxGrid[i][j], boxGrid[i][ind] = boxGrid[i][ind], boxGrid[i][j]
                    ind -= 1
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res