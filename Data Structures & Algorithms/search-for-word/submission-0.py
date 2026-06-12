class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtracking(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]):
                return False

            original = board[row][col]
            board[row][col] = "#"

            # Check all 4 directions
            found = (backtracking(row + 1, col, index + 1) or 
                    backtracking(row - 1, col, index + 1) or 
                    backtracking(row, col + 1, index + 1) or 
                    backtracking(row, col - 1, index + 1))

            board[row][col] = original

            return found
        for r in range(rows):
            for c in range(cols):
                if backtracking(r,c,0):
                    return True
        return False