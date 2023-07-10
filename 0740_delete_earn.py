import cProfile
from typing import List, Dict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_dict = {}
        nums.sort()

        for i in range(len(nums)):
            if nums_dict.get(nums[i]) != None:
                nums_dict[nums[i]] += nums[i]
            else:
                nums_dict[nums[i]] = nums[i]

        score = 0 

        # print(nums_dict)
        score += self.clean_up(nums_dict)
        # print(score)
        # print(nums_dict)
        

        set_list = self.seperate_sets(nums_dict)
        # print(set_list)

        for set in set_list:
            sliced_nums_dict = {}
            if set[1]-set[0] > 1:
                for i in range(set[0], set[1]+1):
                    sliced_nums_dict[i] = nums_dict[i]
                # print(set)
                score+= self.surprise_not_recursion(sliced_nums_dict, set) 
            else:
                score+= max(nums_dict[set[0]], nums_dict[set[1]])   

        return score

    def seperate_sets(self, nums_dict):
        set_list = []
        for i in nums_dict:
            if nums_dict.get(i-1)==None:
                set_list.append([i])
            if nums_dict.get(i+1)==None:
                set_list[-1].append(i)
        return set_list
            
    def clean_up(self, nums_dict):
        clean_up_list = []
        score = 0
        for i in nums_dict:
            if nums_dict.get(i-1)==None and nums_dict.get(i+1)==None:
                clean_up_list.append(i)

        for i in clean_up_list:
            score += self.delete_and_score(i, nums_dict)
        
        return score

    def delete_and_score(self, n, nums_dict):
        score = nums_dict[n]
        # print(n, nums_dict)
        del(nums_dict[n])
        if nums_dict.get(n-1)!=None:
            del(nums_dict[n-1])
        if nums_dict.get(n+1)!=None:
            del(nums_dict[n+1])
        # print(nums_dict)
        return score

    def surprise_not_recursion(self, nums_dict:Dict[int, int], set, solutions_dict = {}):

        solutions_dict[set[0]] = nums_dict[set[0]]
        solutions_dict[set[0]+1] = nums_dict[set[0]+1]
        solutions_dict[set[0]+2] = nums_dict[set[0]] + nums_dict[set[0]+2] 

        for i in range(set[0]+3,set[1]+1):

            solutions_dict[i] = max(solutions_dict[i-3], solutions_dict[i-2])+nums_dict[i]

        # print(solutions_dict)
        
        # print(solutions_dict[set[1]], solutions_dict[set[1]-1])
        return max(solutions_dict[set[1]], solutions_dict[set[1]-1])

def test():
    
    sol = Solution()

    nums = [3, 4, 2]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 6
    print("correct solution")

    nums = [2,2,3,3,3,4]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 9
    print("correct solution")

    nums = [12,32,93,17,100,72,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 1140
    print("correct solution")    
    
    nums = [3,3,3,3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,8,9,9,9,9,9,9,9,9,9,9,10,10,10]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 174
    print("correct solution")

    nums = [10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 338
    print("correct solution")


    nums = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 3451
    print("correct solution")

    nums = [25,95,76,4,90,87,46,44,58,33,62,79,5,3,32,21,87,31,44,68,49,45,18,50,26,74,64,17,81,49,80,58,15,6,90,8,6,28,15,16,9,98,50,96,30,27,67,99,86,63,19,54,80,4,84,24,60,22,75,35,76,3,37,80,16,51,14,51,93,49,84,82,48,9,7,79,7,68,15,11,71,59,18,47,5,57,64,38,99,35,57,9,13,14,81,25,5,14,74,63,80,78,70,48,32,54,34,40,21,95,98,25,72,59,21,49,19,2,18,93,14,81,57,41,95,69,71,64,50,35,26,72,92,51,18,11,55,26,2,95,93,35,71,47,88,22,66,90,72,66,61,11,76,10,95,24,35,75,15,95,24,76,78,58,28,23,75,73,40,40,84,18,31,91,7,97,13,96,39,17,22,85,28,79,61,73,88,36,82,27,95,31,96,59,20,13,44,13,7,29]
    solution = sol.deleteAndEarn(nums=nums)
    print(solution)
    assert solution == 6104
    print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')