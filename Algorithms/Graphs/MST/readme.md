The key idea of Kruskal's Algorithm is to build multiple trees, each of them consists of two nodes and an edge between them. After we do the union on each of them, we will get a MST.
In a word, we'll get a minimum spanning forest first, then merge every two of them.

To do that, we need just 3 steps:

    Hold a list consists of all the nodes in the fomat of (u, v, w), where u and v are two end nodes of a single edge, w stands for the weight.
    Sort the list with the key as weight.
    Pick edges starting from the one with smallest weight, union the two nodes to construct a tree or merge two trees if the two nodes belong to different existing trees.

Basically Kruskal's algorithm is union find plus some modifications, in this problem, we can skip actually implementing the union function, and do the union in the for loop where we pick points to connect.



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        parent = list(range(len(points)))
        g = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                g.append((i, j, abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])))
        
        cost = 0
        for u, v, w in sorted(g, key=lambda x:x[2]):
            ru, rv = find(u), find(v)
            if ru == rv:    # u and v must not be connected for now
                continue
            parent[ru] = rv
            cost += w
        
        return cost

With the code above, the space complexity is O(V), and the time complexity is O(|E| * log|V|).
