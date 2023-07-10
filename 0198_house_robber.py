from typing import List, Dict
import cProfile



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        solution_dict = {
            0: nums[0],
            1: nums[1]
        }


        return max(self.recursive_find_solution(n=len(nums)-1, nums=nums, solution_dict=solution_dict), self.recursive_find_solution(n=len(nums)-2, nums=nums, solution_dict=solution_dict))


    def recursive_find_solution(self, n, nums, solution_dict:Dict[int, int]) -> int:
        
        # print(n)
        if solution_dict.get(n) != None:
            return solution_dict[n]

        if n > 1:
            solution_dict[n] = max(self.recursive_find_solution(n-3, nums, solution_dict), self.recursive_find_solution( n-2, nums,  solution_dict)) + nums[n]
            return solution_dict[n]

        if n<0:
            return 0

        return None



def test():
    sol = Solution()

    nums = [1,2,3,1]
    solution = sol.rob(nums)
    print(solution)
    assert solution == 4

    nums = [2,7,9,3,1]
    solution = sol.rob(nums)
    print(solution)
    assert solution == 12

    nums = [0]
    solution = sol.rob(nums)
    print(solution)
    assert solution == 0




if __name__ == "__main__":
    cProfile.run('test()')