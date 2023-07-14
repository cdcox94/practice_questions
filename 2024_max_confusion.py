from typing import List, Dict
import cProfile

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        window_size = k
        count_dict = {
            "T":0,
            "F":0
        }
        len_answer_key = len(answerKey)

        if len_answer_key - k <= 2:
            return len_answer_key

        for i in range(window_size):
            count_dict[answerKey[i]]+=1

        index = 0  
        while index+window_size < len_answer_key:
            while count_dict["F"] <= k or count_dict["T"] <= k:
                count_dict[answerKey[index+window_size]]+=1
                window_size+=1
                if index+window_size+1 > len_answer_key:

                    if count_dict["F"] <= k or count_dict["T"] <= k:
                        return window_size
                    else:
                        return window_size -1
            count_dict[answerKey[index]] -= 1
            count_dict[answerKey[index+window_size]] += 1
            index += 1

        if count_dict["F"] == k or count_dict["T"] == k:
            return window_size
        else:
            return window_size -1


def test():
    
    sol = Solution()

    answerKey = "TTFF"
    k=2
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 4

    answerKey = "TTFTTFTT"
    k=1
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 5

    answerKey = "TFFT"
    k=1
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 3

    answerKey = "TTTTFFFFFFFTTT"
    k=2
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 9

    answerKey = "FFFTTFTTFT"
    k = 3
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 8

    answerKey = "FFTFTFTFFT"
    k = 6
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 10

    answerKey = "TFTFFFTFTT"
    k = 6
    solution = sol.maxConsecutiveAnswers(answerKey=answerKey, k=k)
    print(solution)
    assert solution == 10


if __name__ == "__main__":
    cProfile.run('test()')