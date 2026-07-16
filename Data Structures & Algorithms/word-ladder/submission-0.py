from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0
        
        wordmap = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i+1:]
                wordmap[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue: 
            curr, level = queue.popleft()

            if curr == endWord: 
                return level
            
            for i in range(len(beginWord)):
                pattern = curr[:i] + "*" + curr[i+1:]

                for neighbor in wordmap[pattern]:
                    if neighbor not in visited: 
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                wordmap[pattern] = []
        return 0
