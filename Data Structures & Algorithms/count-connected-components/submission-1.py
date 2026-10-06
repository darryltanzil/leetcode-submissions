class FindUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def findParent(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, a, b):
        self.parent[self.findParent(a)] = self.findParent(b)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = FindUnion(n)
        
        for a, b in edges:
            dsu.union(a, b)
        
        return len(set(dsu.findParent(i) for i in range(n)))
        