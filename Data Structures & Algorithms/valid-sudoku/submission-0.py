class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col= [[0 for _ in range(9)] for _ in range(9)]
        box= [[0 for _ in range(9)] for _ in range(9)]
        for k in range(9):
            for l in range(9):
                col[k][l] = board[l][k]
                box[k][l] = board[(k//3)*3 +l//3][(k%3)*3 + l % 3]
        print(col)
        print(box)

        for i in range(9):
            col[i].sort()
            board[i].sort()
            box[i].sort()
            for j in range(9-1):
                if i!= j and board[i][j]!= '.' and (board[i][j] == board[i][j+1] or board[i][j] == board[i][j-1]):
                    return False
                if i!= j and col[i][j]!= '.' and (col[i][j] == col[i][j+1] or col[i][j] == col[i][j-1]):
                    return False
                if i!= j and box[i][j]!= '.' and (box[i][j] == box[i][j+1] or box[i][j] == box[i][j-1]):
                    return False
        
        
        return True


        
        