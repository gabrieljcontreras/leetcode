from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1): 
            w1, w2 =  words[i], words[j:= i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2: 
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for neighbor in adj_list[curr]:
                in_degree[neighbor]-=1
                if in_degree[neighbor] == 0: 
                    queue.append(neighbor)

        if len(result) == len(in_degree):
            return "".join(result)
        return ""