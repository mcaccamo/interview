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
