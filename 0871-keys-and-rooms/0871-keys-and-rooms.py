class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #DFS Solution
        def dfs(room):
            if visit[room]:
                return
            visit[room] = True
            for i in rooms[room]:
                dfs(i)
        
        visit = [False] * len(rooms)
        dfs(0)
        return all(visit)
        