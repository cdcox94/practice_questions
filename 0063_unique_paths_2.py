import cProfile
from typing import List, Dict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        solutions_list = []
        for i in range(n):
            solutions_list.append([])
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    if i == 0:
                        if j==0:
                            solutions_list[i].append(1)
                        else:
                            solutions_list[i].append(solutions_list[i][j-1])
                    else:
                        if j == 0:
                            solutions_list[i].append(solutions_list[i-1][j])
                        else:
                            solutions_list[i].append(solutions_list[i-1][j]+solutions_list[i][j-1])
                else:
                    solutions_list[i].append(0)

        print(solutions_list)

        return solutions_list[n-1][m-1]



def test():
    
    sol = Solution()

    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    solution = sol.uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    print(solution)
    assert solution == 2
    print("correct solution")

    obstacleGrid = [[0,1],[0,0]]
    solution = sol.uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    print(solution)
    assert solution == 1
    print("correct solution")

    obstacleGrid = [[1,0]]
    solution = sol.uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    print(solution)
    assert solution == 0
    print("correct solution")

    obstacleGrid = [[1],[0]]
    solution = sol.uniquePathsWithObstacles(obstacleGrid=obstacleGrid)
    print(solution)
    assert solution == 0
    print("correct solution")



if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')