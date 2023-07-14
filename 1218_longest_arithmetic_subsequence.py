import cProfile
import collections
from typing import List, Dict


class Solution:
    
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        solutions_dict = collections.defaultdict(int)
        max_val = 0

        for i in range(len(arr)):
            solutions_dict[arr[i]+difference] = max(solutions_dict[arr[i]+difference], 1 + solutions_dict[arr[i]])
            if solutions_dict[arr[i]+difference]>max_val:
                max_val = solutions_dict[arr[i]+difference]

        return max_val

    def longestSubsequence_slow(self, arr: List[int], difference: int) -> int:
        solutions:List[List[int]] = []

        for i in range(len(arr)):
            for solution in solutions:
                if solution[-1] + difference == arr[i]:
                    solution.append(arr[i])
            solutions.append([arr[i]])

        return max([len(x) for x in solutions])


def test():
    sol = Solution()

    arr = [1,2,3,4]
    difference = 1
    solution = sol.longestSubsequence(arr=arr,difference=difference)
    assert solution == 4
    print("correct solution")

    arr = [1,3,5,7]
    difference = 1
    solution = sol.longestSubsequence(arr=arr,difference=difference)
    assert solution == 1
    print("correct solution")

    arr = [1,5,7,8,5,3,4,2,1]
    difference = -2    
    solution = sol.longestSubsequence(arr=arr,difference=difference)
    assert solution == 4
    print("correct solution")

    arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
    difference = 0
    solution = sol.longestSubsequence(arr=arr,difference=difference)
    assert solution == 2
    print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()')
