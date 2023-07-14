from typing import List, Dict
import cProfile

class Solution:
    def largestVariance(self, s: str) -> int:

        global_max = 0
        global_min = 0
        array_length = len(s)
        # original_set = set(s)
        set1 = set(s)
        set_list1 = [x for x in set1]

        if len(set1) == len(s):
            return 0

        # loop through all unique chars in the set of chars

        while len(set_list1)>1:
            c1 = set_list1[0]
            # print(c1)
            set_list2 = set_list1.copy()
            set_list2.pop(0)
            for c2 in set_list2:
                # print(c1, c2)
                encoded_array = []
                for index in range(array_length):
                    if s[index] == c1:
                        encoded_array.append(1)
                    elif s[index] == c2:
                        encoded_array.append(-1)
                    else:
                        encoded_array.append(0)
                
                # kadenes algorithm
                num_neg = 0 
                num_pos = 0
                local_max = 0
                local_min = 0
                for index in range(array_length):
                    local_max += encoded_array[index]
                    local_min += encoded_array[index]

                    if encoded_array[index] == 1:
                        num_pos += 1
                    if encoded_array[index] == -1:
                        num_neg += 1
                    if local_max>global_max:
                        if  num_neg>0:
                            global_max = local_max
                        else:
                            global_max = local_max - 1

                    if local_min<global_min:
                        if num_pos>0:
                            global_min = local_min
                        else:
                            global_min = local_min + 1

                    if local_min > 0:
                        local_min = 0
                        num_pos = 0
                    if local_max < 0:
                        local_max=0
                        num_neg=0
            set_list1.pop(0)
        # print(global_max)
        # print(encoded_array[start:end])
        # print(start)
        # print(end)
        # print(global_min)
        # print(global_max)
        if abs(global_min)>global_max:
            return abs(global_min)

        return global_max

                

def test():
    
    sol = Solution()

    s = "aababbb"
    solution = sol.largestVariance(s)
    print(solution)
    assert solution == 3

    s = "abcde"
    solution = sol.largestVariance(s)
    print(solution)
    assert solution == 0

    s = "icexiahccknibwuwgi"
    solution = sol.largestVariance(s)
    print(solution)
    assert solution == 3

    s = "lripaa"
    solution = sol.largestVariance(s)
    print(solution)
    assert solution == 1

    s = "serhmxxnljyowqwmeaswybbictfmeqdzybvkrhhigzhzsmg"
    solution = sol.largestVariance(s)
    print(solution)
    assert solution == 3

if __name__ == "__main__":
    cProfile.run('test()')