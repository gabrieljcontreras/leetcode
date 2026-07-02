class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        adj_list = {i: [] for i in range(n)}
        for a, b in edges: 
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited: 
                    dfs(neighbor)
            
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components
