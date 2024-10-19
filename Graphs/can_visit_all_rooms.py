class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        from collections import deque
        q = deque([(0,rooms[0])])
        visited = set()

        while q:
            room_no, rooms_can_visit = q.popleft()
            print(room_no,rooms_can_visit)
            visited.add(room_no)

            for room_to_visit in rooms_can_visit:
                if room_to_visit in visited: continue
                next_rooms_to_visit = rooms[room_to_visit]
                q.append( (room_to_visit,next_rooms_to_visit))
        return len(visited) == len(rooms)



