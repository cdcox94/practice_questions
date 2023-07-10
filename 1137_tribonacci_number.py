from typing import List, Dict
import cProfile



class Solution:
    def tribonacci(self, n: int) -> int:
        solution_dict = {
            0: 0,
            1: 1,
            2: 1,
        }
        return self.recursive_find_solution(n, solution_dict)

    def recursive_find_solution(self, n, solution_dict:Dict[int, int]) -> int:
        
        if solution_dict.get(n) != None:
            return solution_dict[n]

        t1 = self.recursive_find_solution(n-1, solution_dict)
        t2 = self.recursive_find_solution(n-2, solution_dict)
        t3 = self.recursive_find_solution(n-3, solution_dict)
        solution_dict[n] = t1 + t2 + t3
        return solution_dict[n]



def test():
    sol = Solution()


    n = 4
    solution = sol.tribonacci(n)
    print(solution)
    assert solution == 4

    n = 25
    solution = sol.tribonacci(n)
    print(solution)
    assert solution == 1389537


if __name__ == "__main__":
    cProfile.run('test()')