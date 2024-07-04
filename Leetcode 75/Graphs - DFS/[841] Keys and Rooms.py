class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0] * len(rooms)
        visited[0] = 1
        def dfs(rooms, key):
            for i in rooms[key]:
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(rooms, i)
        dfs(rooms, 0)
        for i in range(0, len(rooms)):
            if visited[i] == 0:
                return False
        return True