    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
    
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

------------------------------------------------------------------------------------------------------------------------
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parent = list(range(n))
    rank = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        elif rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[rx] = ry
            rank[ry] += 1
    
    for x, y in edges:
        union(x, y)
    return len({find(i) for i in range(n)})
