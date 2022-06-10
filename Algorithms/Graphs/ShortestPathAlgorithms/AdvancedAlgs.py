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
# Bellman Ford
