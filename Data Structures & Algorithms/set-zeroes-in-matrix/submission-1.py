class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seenrow = set()
        seencols = set()

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows): 
            for c in range(cols): 
                if matrix[r][c] == 0: 
                    seenrow.add(r)
                    seencols.add(c)
        for r in range(rows): 
            for c in range(cols): 
                if r in seenrow or c in seencols: 
                    matrix[r][c] = 0
