from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for course, prereq in prerequisites: 
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        completed = 0

        while queue: 
            curr = queue.popleft()
            completed += 1

            for next_course in adj_list[curr]:
                in_degree[next_course] -= 1

                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return completed == numCourses