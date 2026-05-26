class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            duplicates = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in duplicates:
                        return False
                    duplicates.add(board[i][j])
        #supposedly each row
        
        for i in range(len(board[i])):
            duplicates = set()
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] in duplicates:
                        return False
                    duplicates.add(board[j][i])
        #each col maybe?

        return True
        #idk how to do 3x3 but this is my like thinking process at least