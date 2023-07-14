import collections
from sys import maxsize
from typing import List, Dict, Optional
import cProfile

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        global_optimal = 9999999999999
        k_list = []
        for i in range(k):
            k_list.append(0)
        
        cookies.sort(reverse=True)
        return self.backtracting_recursion(cookies=cookies, k_list=k_list, global_optimal=global_optimal)
    
    def backtracting_recursion(self, cookies, k_list, global_optimal):
        
        if len(cookies) == 0:
            return max(k_list)
        
        for i in range(len(k_list)):
            k_list_c = k_list.copy()
            k_list_c[i] += cookies[-1]
            if k_list_c[i]>=global_optimal:
                continue
            local_optima = self.backtracting_recursion(cookies[:-1], k_list=k_list_c, global_optimal=global_optimal)
            if local_optima < global_optimal:
                global_optimal = local_optima
        
        return global_optimal

def test():
    
    sol = Solution()
    
    cookies = [8,15,10,20,8]
    k = 2
    solution = sol.distributeCookies(cookies=cookies, k=k)
    print(solution)
    assert solution == 31

    cookies = [6,1,3,2,2,4,1,2]    
    k = 3
    solution = sol.distributeCookies(cookies=cookies, k=k)
    print(solution)
    assert solution == 7

    cookies = [6,1]    
    k = 2
    solution = sol.distributeCookies(cookies=cookies, k=k)
    print(solution)
    assert solution == 6


if __name__ == "__main__":
    cProfile.run('test()')