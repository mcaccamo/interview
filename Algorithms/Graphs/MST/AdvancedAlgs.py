# Prims


def minCostConnectPoints(self, points: List[List[int]]) -> int:
     N = len(points)
     adj = { i:[] for i in range(N) } # i : list of [cost, node]
     
     #for every pair of points, calcualte the distance between them (i.e. cost from a->b or vice-versa)
     for i in range(N): 
         x1, y1 = points[i]
         for j in range(i + 1, N):
             x2, y2 = points[j]
             dist = abs(x1 - x2) + abs(y1 - y2)
             adj[i].append([dist, j])
             adj[j].append([dist, i])
     
     # Prim's
     res = 0
     visit = set()
     minH = [[0, 0]] # [cost, point] (choose any point to start with. Distance to incldue a source point is 0. 
     #We are choosing vertice 0 here but could choose any of the n points)
     while len(visit) < N:
         cost, i = heapq.heappop(minH)
         if i in visit: # if you would be adding an edge you've added to the MST already, skip
             continue
         res += cost
         visit.add(i)
         for neiCost, nei in adj[i]:
             if nei not in visit:
                 heapq.heappush(minH, [neiCost, nei])
     return res
# Kruskals


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        self.parent[pu] = pv
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([manhattanDist(points[i], points[j]), i, j])

        edges.sort()  # Sort increasing order by dist
        uf = UnionFind(n)
        ans = 0
        for d, u, v in edges:
            if uf.union(u, v):
                ans += d
                n -= 1
            if n == 1: break  # a bit optimize when we found enough n-1 edges!
        return ans
