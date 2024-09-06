class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)] # prereq --> next course
        indegree = [0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        from collections import deque
        q = deque([i for i in range(numCourses) if indegree[i] == 0]) # course with no prereqs
        ordering = []
        while q:
            prereq = q.popleft()
            numCourses -= 1
            ordering.append(prereq)
            for next_course in graph[prereq]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: q.append(next_course)
        return ordering if numCourses == 0 else []