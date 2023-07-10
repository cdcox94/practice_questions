from typing import List, Dict
import cProfile

class Solution:
    def climbStairs(self, n: int) -> int:
        solution_dict = {
            1: 1,
            2: 2
        }
        return self.recursive_find_solution(n, solution_dict)


    def recursive_find_solution(self, n, solution_dict:Dict[int, int]) -> int:
        
        if solution_dict.get(n):
            return solution_dict[n]

        if n > 2:
            solution_dict[n] = self.recursive_find_solution(n-2, solution_dict) + self.recursive_find_solution( n-1, solution_dict)
            return solution_dict[n]

        return None


def test():
    sol = Solution()

    n=2
    solution = sol.climbStairs(n)
    print(solution)
    assert solution == 2
    print("correct solution")

    n=3
    solution = sol.climbStairs(n)
    print(solution)
    assert solution == 3
    print("correct solution")

    n=8
    solution = sol.climbStairs(n)
    print(solution)
    assert solution == 34
    print("correct solution")

if __name__ == "__main__":
    cProfile.run('test()')