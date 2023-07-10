import collections
from typing import List, Dict, Optional
import cProfile

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k:int ) -> int:
        left = 0
        right = 0
        count = collections.defaultdict(int)
        distinct = 0
        string_length = len(s)
        while right < string_length:
            if count[s[right]] == 0:
                distinct+=1
            count[s[right]] += 1
            right+=1 

            if distinct>k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    distinct-=1
                left+=1

        return right-left


    def lengthOfLongestSubstringKDistinct2(self, s: str, k: int) -> int:
        
        if k == 0:
            return 0
        
        if len(set(s)) <= k:
            return len(s)
        
        
        window_contents = {}
        window_size = k
        index = 0
        distinct = 0

        # preload contents
        for i in range(window_size):
            if window_contents.get(s[i])==None:
                window_contents[s[i]] = 1
                distinct+=1
            else:
                window_contents[s[i]] += 1
            

        while index+window_size < len(s):

            while distinct <= k:
                temp = window_contents.get(s[index+window_size])
                if temp == None:
                    window_contents[s[index+window_size]] = 1
                    distinct+=1
                elif temp == 0:
                    window_contents[s[index+window_size]] = 1
                    distinct+=1
                else:
                    window_contents[s[index+window_size]] += 1

                window_size+=1
                if index+window_size>=len(s):
                    if distinct == k:
                        return window_size
                    else:
                        return window_size -1

            window_contents[s[index]] -= 1
            if window_contents[s[index]] == 0:
                distinct -= 1
            
            if index+window_size < len(s):
                temp = window_contents.get(s[index+window_size])
                if temp == None:
                    window_contents[s[index+window_size]] = 1
                    distinct+=1
                elif temp == 0:
                    window_contents[s[index+window_size]] = 1
                    distinct+=1
                else:
                    window_contents[s[index+window_size]] += 1
                index+=1

            else:
                # print('here')
                if sum(window_contents.values())==k:
                    window_size-=1
                break
        
        if distinct == k:
            return window_size
        else:
            return window_size -1

def test():
    
    sol = Solution()
    
    s = "eceba"
    k = 2
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 3

    s = "aa"
    k = 1
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 2

    s = "abcabc"
    k = 3
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 6

    s = "a"
    k = 0
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 0

    s = "a"
    k = 2
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 1

    s = "ab"
    k = 1
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 1

    s = "abee"
    k = 1
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 2

    s = "aac"
    k = 1    
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 2

    s = "ababacccccc"
    k = 2 
    solution = sol.lengthOfLongestSubstringKDistinct(s, k)
    print(solution)
    assert solution == 7

if __name__ == "__main__":
    cProfile.run('test()')