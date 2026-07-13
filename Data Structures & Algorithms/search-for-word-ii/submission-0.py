class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words: 
            node = root
            for char in word: 
                if char not in node.children: 
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end  = True
            node.word = word
        
        result = []
        rows, cols = len(board), len(board[0])

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children: 
                return
            
            next_node = node.children[char]

            if next_node.is_end: 
                result.append(next_node.word)
                next_node.is_end = False
            
            board[r][c] = "#"

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)

            board[r][c] = char

            if not next_node.children: 
                del node.children[char]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return result