class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # Initialize indegrees and graph
        indegrees = {}
        for n in range(0, numCourses):
            indegrees[n] = 0
        graph = {}
        for n in range(0, numCourses):
            empty_array = []
            graph[n] = empty_array

        # build graph and indegrees dictionaries
        for eachPrereq in prerequisites:
            graph[eachPrereq[1]].append(eachPrereq[0])
            indegrees[eachPrereq[0]] += 1

        # initalize queue with all nodes that have indegree = 0
        q = []
        for course in indegrees:
            if indegrees[course] == 0:
                q.append(course)
        if not q:
            return False
        visited = set()

        # Topological Sort
        while len(q) != 0:
            course = q.pop(0)
            visited.add(course)
            for nextCourse in graph[course]:
                indegrees[nextCourse] -= 1
                if indegrees[nextCourse] == 0:
                    q.append(nextCourse)

        # check to see if we've visited all nodes
        return len(visited) == numCourses
