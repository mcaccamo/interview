    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #  build adj_list for each node
        # Iterate over (unvistited) n, incrementing a counter for every iteration, marking nodes as visisted
        # after all nodes are visited, counter == num componentes
        
        if not edges:
            return n
        
        def markNeighborsVisited(adj_list, node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
            #        visited.add(neighbor)
                    markNeighborsVisited(adj_list, neighbor, visited)
                
        adj_list = collections.defaultdict(list)
        
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = set()
        counter = 0
        for i in range(n):
            if i not in visited:
                counter+=1
                markNeighborsVisited(adj_list, i, visited)
                
                
        return counter
