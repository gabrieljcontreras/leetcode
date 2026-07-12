class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diagonal = set()
        neg_diagonal = set()

        res = []

        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n: 
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in cols or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue 

                cols.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c] = "Q"
                
                dfs(r+1)

                cols.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res
