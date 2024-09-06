class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step 1: get all courses with an indegree of zero
        # step 2: add those in your topological ordering
        # step 3: remove all those nodes and its corresponding edges for ex: s --> __
        # step 4: do step 1 until all courses are finished (numCourses == 0)
        # IF YOU DONT GET INDEGREE COURSES cannot finish

        # you need indegree and adjacency list
        graph = [[] for _ in range(numCourses)] # prereq --> next course
        indegree = [0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        from collections import deque
        q = deque([i for i in range(numCourses) if indegree[i] == 0]) # course with no prereqs

        while q:
            prereq = q.popleft()
            numCourses -= 1
            for next_course in graph[prereq]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: q.append(next_course)
        return numCourses == 0
        
