import cProfile
from typing import List, Dict


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        solution=[triangle[-1]]
        for i in range(1,len(triangle)):
            solution.append([])
            for j in range(len(triangle[-i-1])):
                # print(triangle[-i-1][j])
                solution[i].append(min(solution[i-1][j], solution[i-1][j+1])+triangle[-i-1][j])

        return solution[-1][-1]



def test():
    
    sol = Solution()

    triangle = [[2],[3,1],[6,5,1],[4,1,8,3]]
    solution = sol.minimumTotal(triangle=triangle)
    print(solution)
    assert solution == 7
    print("correct solution")

    triangle = [[-10]]
    solution = sol.minimumTotal(triangle=triangle)
    print(solution)
    assert solution == -10
    print("correct solution")
    
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    solution = sol.minimumTotal(triangle=triangle)
    print(solution)
    assert solution == 11
    print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')