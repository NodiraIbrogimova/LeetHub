class Solution:
     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        # The BFS version
        # create an adjacency matrix
        adjacent_matrix = []
        for node in range(n):
            adjacent_matrix.append(set())
            
        for start, end in edges:
            adjacent_matrix[start].add(end)
            adjacent_matrix[end].add(start)
                
        
        length = len(adjacent_matrix)
        leaves = []
        # initialize the first layer of the leaves
        for node in range(n):
            if len(adjacent_matrix[node]) == 1:
                leaves.append(node)
                
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adjacent_matrix[leaf].pop()
                adjacent_matrix[neighbor].remove(leaf)
                if len(adjacent_matrix[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
                
                
        
        '''    
        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        print('neighbors: ', neighbors)
        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        print('leaves: ', leaves)
        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            print('rem nodes: ', leaves)
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                
                leaf = leaves.pop()
                print('\npop leaf: ', leaf)
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                print('neighbors: ', neighbors)
                print('neighbor: ', neighbor)
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves
        print('result ', leaves)
        return leaves
#     def find_farthest(self, start, n, Graph):
#         self.dist, self.parent = [-1]*n, [-1]*n
#         self.dist[start] = 0
#         self.dfs(start, Graph)
#         return self.dist.index(max(self.dist))
    
#     def dfs(self, start, Graph):
#         for neighbor in Graph[start]:
#             if self.dist[neighbor] == -1:
#                 self.dist[neighbor] = self.dist[start] + 1
#                 self.parent[neighbor] = start
#                 self.dfs(neighbor, Graph)

#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         # create an adjacency list
#         Graph = defaultdict(set)
#         for a,b in edges:
#             Graph[a].add(b)
#             Graph[b].add(a)
            
#         print('graph: ', Graph)
        
#         node_1 = self.find_farthest(0, n, Graph)
#         node_2 = self.find_farthest(node_1, n, Graph)
        
#         path = []
#         while node_2 != -1:
#             path.append(node_2)
#             node_2 = self.parent[node_2]
            
#         Q = len(path)
#         return list(set([path[Q//2], path[(Q-1)//2]]))
        '''