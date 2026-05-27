class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            duplicates = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in duplicates:
                    return False
                duplicates.add(board[row][col])
        #supposedly each row
        
        for col in range(9):
            duplicates = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in duplicates:
                    return False
                duplicates.add(board[row][col])
        #each col maybe?

        for square in range(9):
            duplicates = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in duplicates:
                        return False
                    duplicates.add(board[row][col])
            
        return True
        # saw solution