import cProfile
from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        cleaned = self.clean_up(requests)
        return self.try_it(n, requests) + cleaned

    def clean_up(self, requests):
        cleaned = 0
        for index in range(len(requests)-1,-1,-1):
            # print(index)
            if requests[index][0] == requests[index][1]:
                requests.pop(index)
                cleaned += 1
        print(f'cleaned up {cleaned}')
        return cleaned

    def try_it(self, n, requests):
        num_unique_solutions = 2**len(requests)
        # print(f"{num_unique_solutions} unique solutions")
        best_solution = 0
        for i in range(num_unique_solutions):
            net_dict = {}
            for j in range(n):
                net_dict[j] = 0
        
            counter = 0 
            for j in range(len(requests)):
                if i >> j & 1:
                    # print(f'request {requests[j]}')
                    net_dict[requests[j][0]] -= 1
                    net_dict[requests[j][1]] += 1
                    # print(net_dict)
                    counter+=1
            
            failed = False
            for j in range(n):
                if net_dict[j] != 0:
                    # print(f'solution {i} failed on index {j}')
                    failed = True
            
            if not failed and counter > best_solution:
                # print(f'new best {counter}')
                best_solution = counter
        # print(f'best solution is {best_solution}')
        return best_solution


def test():
    sol = Solution()

    n = 5
    requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 5

    n = 3
    requests = [[0,0],[1,2],[2,1]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 3

    n = 4
    requests = [[0,3],[3,1],[1,2],[2,0]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 4

    n = 5
    requests = [[2,1],[0,1],[1,2],[2,0]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 3

    n = 2
    requests = [[1,1],[1,0],[0,1],[0,0],[0,0],[0,1],[0,1],[1,0],[1,0],[1,1],[0,0],[1,0]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 11

    n = 4
    requests = [[0,0],[1,3],[1,3],[2,3],[1,0],[2,2],[1,2],[2,1],[1,3],[0,2],[3,0],[3,1],[2,2],[3,0],[0,3],[3,1]]
    solution = sol.maximumRequests(n, requests)
    print(solution)
    assert solution == 14


if __name__ == "__main__":
    cProfile.run('test()')