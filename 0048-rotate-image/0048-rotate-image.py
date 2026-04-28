class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


# or for tie we can use 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       
         r=-1
        c=0
        matrix1 = copy.deepcopy(matrix) 
        for i in range (len(matrix[0])):
            r+=1
            for j in range (len(matrix)-1,-1,-1):

                matrix[r][c]=matrix1[j][i]
                c+=1
                if c==len(matrix):
                    c=0
    
