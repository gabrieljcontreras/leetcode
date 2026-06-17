class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.tree = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.tree
        for c in word: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
    def search(self, word: str) -> bool:
        def dfs(index, node):

            curr = node
            for i in range(index, len(word)): 
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else: 
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end
        return dfs(0, self.tree)
        
