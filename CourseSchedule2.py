class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        if not prerequisites:
            for n in range(0, numCourses):
                output.append(n)
            return output

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
            return output
        visited = set()

        # Topological Sort
        while len(q) != 0:
            course = q.pop(0)
            output.append(course)
            visited.add(course)
            for nextCourse in graph[course]:
                indegrees[nextCourse] -= 1
                if indegrees[nextCourse] == 0:
                    q.append(nextCourse)

		# check to see if we've visited all nodes
        # if not, it is impossible to finish all courses
        if len(visited) == numCourses:
            return output
        else:
            return []
        
