from typing import List, Dict
import cProfile


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt_dict = self.create_debt_dict()

        for transaction in transactions:
            debt_dict[transaction[0]] -= transaction[2]
            debt_dict[transaction[1]] += transaction[2]

        # print(debt_dict)

        pos_balance = []
        neg_balance = []
        for i in range(12):
            if debt_dict[i] > 0:
                pos_balance.append(i)
            elif debt_dict[i] < 0:
                neg_balance.append(i)

        min_val, max_count = self.recursion_woo(pos_balance=pos_balance, neg_balance=neg_balance, debt_dict=debt_dict, best= 100)        


        if min_val == 101:
            return 0
        else:
            return min_val

    def recursion_woo(self, pos_balance:List[int], neg_balance:List[int], debt_dict:Dict[int, int], best, recursion_count = 0):
        
        min_val = 100

        if recursion_count>best:
            # print("fuckit")
            return 100, best
        
        if recursion_count+max([len(pos_balance), len(neg_balance)])>best:
            # print("fucked it")
            return 100, best

        for i in range(len(pos_balance)):
            for j in range(len(neg_balance)):
                
                debt_dict_c = debt_dict.copy()
                pos_balance_c = pos_balance.copy()
                neg_balance_c = neg_balance.copy()
                
                debt_dict_c[pos_balance_c[i]] += debt_dict_c[neg_balance_c[j]]
                debt_dict_c[neg_balance_c[j]] = 0
                
                neg_balance_c.pop(j)
                if debt_dict_c[pos_balance_c[i]] < 1:
                    if debt_dict_c[pos_balance_c[i]] < 0:
                        neg_balance_c.append(pos_balance_c[i])
                    pos_balance_c.pop(i)

                # print("pos balance len", len(pos_balance_c))
                if len(pos_balance_c) == 0:
                    # print("returning", recursion_count)
                    return 1, recursion_count
                else:
                    # print("dict", debt_dict_c)
                    # print("pos", pos_balance_c)
                    # print("neg", neg_balance_c)
                    # print("here", best)
                    transactions, max_count = self.recursion_woo(pos_balance_c, neg_balance_c, debt_dict_c, best, recursion_count=recursion_count+1)

                if transactions < min_val:
                    min_val = transactions
                if max_count<best:
                    # print(best)
                    best = max_count
                    # print(best)

        return min_val+1, best

    
    def create_debt_dict(self):
        debt_dict = {}
        for i in range(12):
            debt_dict[i] = 0
        return debt_dict
    


def test():
    sol = Solution()

    transactions = [[0,1,10],[2,0,5]]
    solution = sol.minTransfers(transactions)
    print(solution)
    assert solution == 2
    print("correct solution")

    transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
    solution = sol.minTransfers(transactions)
    print(solution)
    assert solution == 1
    print("correct solution")

    transactions = [[0,3,10],[1,2,7],[2,1,5],[3,2,5],[4,0,5]]
    solution = sol.minTransfers(transactions)
    print(solution)
    assert solution == 3
    print("correct solution")

    transactions = [[1,8,1],[1,0,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,1,59],[7,0,60]]
    solution = sol.minTransfers(transactions)
    print(solution)
    assert solution == 8
    print("correct solution")

if __name__ == "__main__":
    cProfile.run('test()')