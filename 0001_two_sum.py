from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i in range(len(nums)):
            if index_dict.get(nums[i]) == None:
                index_dict[nums[i]] = i
            else:
                if type(index_dict[nums[i]]) == list:
                    index_dict[nums[i]].append(i)
                else:
                    index_dict[nums[i]] = [index_dict[nums[i]], i]

        for i in range(len(nums)):
            sol = index_dict.get(target-nums[i])
            if sol != None:
                if type(sol) == list:
                    for j in range(len(sol)):
                        if i == sol[j]:
                            continue
                        else:
                            return [i, sol[j]]
                if i == sol:
                    continue
                return [i, sol]
            



def test():
    
    sol = Solution()

    nums = [2,7,11,15]
    target = 9
    solution = sol.twoSum(nums, target)
    print(solution)
    assert solution == [0,1]

    nums = [3,2,4]
    target = 6
    solution = sol.twoSum(nums, target)
    print(solution)
    assert solution == [1,2]

    nums = [3,3]
    target = 6
    solution = sol.twoSum(nums, target)
    print(solution)
    assert solution == [0,1]



if __name__ == "__main__":
    test()