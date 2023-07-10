import cProfile
from typing import List, Dict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        solutions_list = []
        for i in range(n):
            solutions_list.append([1])
            if i == 0:
                for j in range(1,m):
                    solutions_list[0].append(1)
            else:
                for j in range(1,m):
                    solutions_list[i].append(solutions_list[i-1][j]+solutions_list[i][j-1])


        return solutions_list[n-1][m-1]



def test():
    
    sol = Solution()

    m = 3
    n = 7
    solution = sol.uniquePaths(m=m, n=n)
    print(solution)
    assert solution == 28
    print("correct solution")

    m = 3
    n = 2
    solution = sol.uniquePaths(m=m, n=n)
    print(solution)
    assert solution == 3
    print("correct solution")



if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')