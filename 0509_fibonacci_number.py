from typing import List, Dict
import cProfile



class Solution:
    def fib(self, n: int) -> int:
        solution_dict = {
            0: 0,
            1: 1
        }
        return self.recursive_find_solution(n, solution_dict)


    def recursive_find_solution(self, n, solution_dict:Dict[int, int]) -> int:
        

        if solution_dict.get(n) != None:
            # print(solution_dict[n])
            return solution_dict[n]

        if n > 1:
            solution_dict[n] = self.recursive_find_solution(n-2, solution_dict) + self.recursive_find_solution( n-1, solution_dict)
            return solution_dict[n]

        return None


def test():
    sol = Solution()


    n = 2
    solution = sol.fib(n)
    print(solution)
    assert solution == 1

    n = 3
    solution = sol.fib(n)
    print(solution)
    assert solution == 2

    n = 4
    solution = sol.fib(n)
    print(solution)
    assert solution == 3



if __name__ == "__main__":
    cProfile.run('test()')