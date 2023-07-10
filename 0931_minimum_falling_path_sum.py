import cProfile
from typing import List, Dict


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m ==1:
            return m[0][0]
        for i in range(1,m):
            for j in range(m):
                if j==0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==m-1:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])

        return min(matrix[-1])



def test():
    
    sol = Solution()

    matrix  = [[2,1,3],[6,5,4],[7,8,9]]
    solution = sol.minFallingPathSum(matrix =matrix )
    print(solution)
    assert solution == 13
    print("correct solution")

    matrix  = [[-10]]
    solution = sol.minFallingPathSum(matrix =matrix )
    print(solution)
    assert solution == -10
    print("correct solution")
    
    matrix  = [[-19,57],[-40,-5]]
    solution = sol.minFallingPathSum(matrix =matrix )
    print(solution)
    assert solution == -59
    print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')