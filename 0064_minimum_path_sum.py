import cProfile
from typing import List, Dict


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        solutions_list = []
        for i in range(n):
            solutions_list.append([])
            for j in range(m):
                if i == 0:
                    if j == 0:
                        solutions_list[i].append(grid[i][j])
                    else:
                        solutions_list[i].append(grid[i][j]+solutions_list[i][j-1])
                else:
                    if j==0:
                        solutions_list[i].append(grid[i][j]+solutions_list[i-1][j])
                    else:
                        solutions_list[i].append(grid[i][j]+min(solutions_list[i-1][j], solutions_list[i][j-1]))

        print(solutions_list)
        return solutions_list[n-1][m-1]



def test():
    
    sol = Solution()

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    solution = sol.minPathSum(grid)
    print(solution)
    assert solution == 7
    print("correct solution")

    grid = [[1,2,3],[4,5,6]]
    solution = sol.minPathSum(grid=grid)
    print(solution)
    assert solution == 12
    print("correct solution")

    grid = [[1]]
    solution = sol.minPathSum(grid=grid)
    print(solution)
    assert solution == 1
    print("correct solution")




if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')