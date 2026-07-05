class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self,node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, n1,n2):
        p1,p2 = self.find(n1), self.find(n2)

        if p1 == p2: 
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else: 
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
       n = len(edges)
       dsu = DSU(n+1)

       for u, v in edges: 
        if not dsu.union(u,v):
            return [u,v] 