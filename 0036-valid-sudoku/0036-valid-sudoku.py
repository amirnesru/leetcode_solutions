class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [x for x in board[i] if x != '.']
            if len(row) != len(set(row)):
                return False
        for i in range(9):
            col = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(col) != len(set(col)):
                return False
        for i in range(9):
            box = []
            row_sta = (i // 3) * 3
            col_sta = (i % 3) * 3
            for r in range(3):
                for c in range(3):
                    val = board[row_sta + r][col_sta + c]
                    if val != '.':
                        box.append(val)

                    if len(box) != len(set(box)):
                        return False
        return True               
            
