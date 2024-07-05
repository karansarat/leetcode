class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(-u)

        visited = [False] * n
        def dfs(u, adj, visited):
            edges = 0
            visited[u] = True
            for v in adj[u]:
                if not visited[abs(v)]:
                    edges += (v > 0) + dfs(abs(v), adj, visited)
            return edges
        
        num = dfs(0, adj, visited)
        return num
 
        
        
            