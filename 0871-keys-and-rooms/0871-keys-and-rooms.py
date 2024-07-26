class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #BFS Solutions
        visit = [False] * len(rooms)
        queue = deque([0])
        visit[0] = True

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if not visit[key]:
                    queue.append(key)
                    visit[key] = True
        
        return all(visit)