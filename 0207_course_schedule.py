import cProfile
import collections
from typing import List, Dict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        edges = prerequisites
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(bool)
        safe = set()

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            t = graph[edges[i][1]]

        print(graph)

        for node in graph.keys():
            if visited[node] == False:
                if not self.depth_first_search(node = node, graph=graph, visited=visited, safe=safe):
                    return False

        return True
    
    def depth_first_search(self, node:int, graph:Dict[int, List[int]], visited:Dict[int, bool], safe:set):
            # visit the node
            visited[node] = True
            # get the neighbors
            adj = graph[node]
            # if there are no neighbors the spot is safe
            if adj == []:
                safe.add(node)
                return True
            
            # if there are neighbors 
            # for each neighbor check if neighbor is safe
            for neighbor in adj:
                # if neighbor has not been visited
                if not visited[neighbor]:
                        # check if neighbor is safe, if the neighbor is not safe, this node is not safe
                        if not self.depth_first_search(node=neighbor, graph=graph, visited=visited, safe=safe):
                             return False
                # if the neighbor has been visited
                else:
                    # if the neighbor is not safe, this node is not safe
                    if not neighbor in safe:
                        return False
            
            # if every neighbor is safe, this node is safe 
            safe.add(node)
            return True

def test():
    
    sol = Solution()


    graph = [[1,0],[0,1]]
    numCourses = 2
    solution = sol.canFinish(numCourses=numCourses, prerequisites=graph)
    print(solution)
    assert solution == False
    print("correct solution")

    numCourses = 2
    graph = [[1,0]]
    solution = sol.canFinish(numCourses=numCourses, prerequisites=graph)
    print(solution)
    assert solution == True
    print("correct solution")



if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')