import cProfile
from typing import List, Dict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        return int((sum(set(nums))*3 - sum(nums))/2)

        nums_dict = {}

        for num in nums:
            if nums_dict.get(num)==None:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            if nums_dict[num] == 3:
                del(nums_dict[num])

        return [x for x in nums_dict][0]




# min square = 1 max square = min(m,n)

def test():
    
    sol = Solution()

    nums = [2,2,3,2]
    solution = sol.singleNumber(nums =nums)
    print(solution)
    assert solution == 3
    print("correct solution")

    nums = [0,1,0,1,0,1,99]
    solution = sol.singleNumber(nums =nums)
    print(solution)
    assert solution == 99
    print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')