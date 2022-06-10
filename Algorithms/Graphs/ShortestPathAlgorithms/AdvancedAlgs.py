# Djikastras
#http://nmamano.com/blog/dijkstra/dijkstra.html

#Typically Dijkstra using a heap-like data structure that supports updating the priority for a given node
# however, this type of priority update is not supported in typical built-in implementations of a heap
# in this case, every edge is added the priority queue, but if a node is reached and processed, it is marked as such
# when an edge to a visited vertex is popped from the heap it is simply skipped. Effectively this means that the heap operates in the same way
# as if it did support a priority update for already inserted nodes. 
#  The trade-off here is a simpler implementation for a slightly larger memory footprint. 
# LazyDijkstra uses O(|E|) space for the heap, TextBook Dijkstra would only use O(|V|). 

def lazyDijkstra(G, s):
    n = len(G)
    INF = 9999999
    dist = [INF for u in range(n)]
    dist[s] = 0
    vis = [False for u in range(n)]
    PQ = [(0, s)]
    while len(PQ) > 0:
        _, u = heappop(PQ) #only need the node, not the distance
        if vis[u]: continue #not first extraction
        vis[u] = True
        for v, l in G[u]:
            if dist[u]+l < dist[v]:
                dist[v] = dist[u]+l
                heappush(PQ, (dist[u]+l, v))
    return dist

#Example of Dijkstra with a slight twist:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = collections.defaultdict(list) # {s: (d, w)}
        for s, d, w in flights: # O(|E|)
            adj[s].append((d,w))
            
        q = [(0, 0, src)]
        distances = [float("inf") for _ in range(n)]
        bestVisited = defaultdict(lambda : math.inf)
        
        while q:
            cost, numStops, node = heapq.heappop(q)
            if numStops >= bestVisited[node]: continue
            
            bestVisited[node] = numStops
            
            if node == dst:
                return cost
            if numStops == k+1:
                continue
            
            for nei, Wi in adj[node]:
                heapq.heappush(q, (cost + Wi, numStops+1, nei))
            
        return -1
# Floyd-Warshall

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [[float("inf") for _ in range(N)] for _ in range(N)]
        for u, v, w in times:
            dist[u-1][v-1] = w
        for i in range(N):
            dist[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        return max(dist[K-1]) if max(dist[K-1]) < float("inf") else -1

# Bellman Ford
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        dist[K-1] = 0
        for _ in range(N-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        return max(dist) if max(dist) < float("inf") else -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights: # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]
