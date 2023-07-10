from typing import List, Dict
import cProfile



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        solution_dict = {
            0: 0,
            1: cost[-1],
            2: cost[-2]
        }

        self.recursive_find_solution(n=len(cost), cost=cost, solution_dict=solution_dict)
        print(solution_dict)

        return min([solution_dict[len(cost)], solution_dict[len(cost)-1]])


    def recursive_find_solution(self, n, cost, solution_dict:Dict[int, int]) -> int:
        
        if solution_dict.get(n) != None:
            return solution_dict[n]

        if n > 2:
            solution_dict[n] = min(self.recursive_find_solution(n-2, cost, solution_dict), self.recursive_find_solution( n-1, cost,  solution_dict)) + cost[-n]
            return solution_dict[n]

        return None



def test():
    sol = Solution()

    cost = [0,0,0,0]
    solution = sol.minCostClimbingStairs(cost)
    print(solution)
    assert solution == 0

    cost = [1,100,1,1,1,100,1,1,100,1]
    solution = sol.minCostClimbingStairs(cost)
    print(solution)
    assert solution == 6

    cost = [10,15,20]
    solution = sol.minCostClimbingStairs(cost)
    print(solution)
    assert solution == 15


if __name__ == "__main__":
    cProfile.run('test()')