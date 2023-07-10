from typing import List, Dict
import cProfile

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        k_array = []

        for i in range(1, len(weights)):
            weight_val = weights[i-1] + weights[i]
            k_array.append(weight_val)
            # self.insertion_sort(weight_val, k_array)
        

        k_array.sort()
        # print(k_array)

        max_score = sum(k_array[-1:-k:-1]) 
        min_score = sum(k_array[0:k-1])

        return max_score - min_score

    def insertion_sort(self, num, array:List[int]):
        
        min_index = 0 
        max_index = len(array)
        current_index = int(0.5*max_index+0.5*min_index)

        if max_index<1:
            array.append(num)
            return
        while max_index - min_index != 1:
            if array[current_index]<num:
                min_index = current_index
                current_index = int(0.5*max_index+0.5*min_index)
            elif array[current_index]>num:
                max_index = current_index
                current_index = int(0.5*max_index+0.5*min_index)
            else:
                array.insert(current_index, num)
                return
        if num>array[max_index-1]:
            array.insert(max_index, num)
        elif num<=array[max_index-1]:
            array.insert(max_index-1, num)

def test():
    
    sol = Solution()

    weights = [1,3,5,1]
    k = 2
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 4

    weights = [1, 3]
    k = 2
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 0

    weights = [4,7,8,3,2,1,10,4]
    k =3
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 21

    weights = [1,4,2,5,2]
    k = 3
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 3

    weights = [45,56,24,8,65,60,6,13,51,26,34,46,61,73,22,27,8,21,21,44]
    k = 17
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 286

    weights = [46,37,46,17,40,50,54,11,1,25,43,21,31,29,58,49,73,54,5,52,73,54,6,22,58,9,34,21,58,68,63]
    k = 30
    solution = sol.putMarbles(weights, k)
    print(solution)
    assert solution == 119

if __name__ == "__main__":
    cProfile.run('test()')