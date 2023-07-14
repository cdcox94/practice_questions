import cProfile
from typing import List, Dict

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        wrong_list = []
        if len(s) != len(goal):
            return False
        for index in range(len(s)):
            char1 = s[index]
            char2 = goal[index]
            if not char1==char2:
                wrong_list.append([char1, char2])

        len_wrong_list = len(wrong_list)

        if len_wrong_list == 0:
            if len(set(s))<len(s):
                return True
        elif len_wrong_list == 2:
            if wrong_list[0][0] == wrong_list[1][1] and wrong_list[0][1] == wrong_list[1][0]:
                return True
        
        return False

    
    # bit mask number of chars that are wrong
    # if chars = 0 
    #   check if has two of same char
    # if chars = 2 
    #   check if they can swap
    # else return false



def test():
    
    sol = Solution()

    s = "ab"
    goal = 'ba'
    solution = sol.buddyStrings(s=s,goal=goal)
    # print(solution)
    assert solution == True
    # print("correct solution")

    s = "ab"
    goal = 'ab'
    solution = sol.buddyStrings(s=s,goal=goal)
    # print(solution)
    assert solution == False
    # print("correct solution")
    
    s = "ab"
    goal = 'ba'
    solution = sol.buddyStrings(s=s,goal=goal)
    # print(solution)
    assert solution == True
    # print("correct solution")

    s = "ab"
    goal = "babbb"
    solution = sol.buddyStrings(s=s,goal=goal)
    # print(solution)
    assert solution == False
    # print("correct solution")

    
    s = "babbbsdaslkjdfhaljsdhflajhsdlkfjaldskfjhalksjdhflakjshdlfkjahsldkjfhlkjsdhflakjshdflkjahdlfkjhalkdjfhlkjashdfljahdflkjahldkfhalskjdfhlkjdhflkjhdslfkjadljkfhlakjdflhkdjhflakdjhflakjdshflkjhsdlfkjhalkjdfhlakjhflkjhalsjdhflakjhdfljahsldkjfhalkjdfhlakjhflksdhflkjsdhlfkjalhf"
    goal = "babbbsdaslkjdfhaljsdhflajhsdlkfjaldskfjhalksjdhflakjshdlfkjahsldkjfhlkjsdhflakjshdflkjahdlfkjhalkdjfhlkjashdfljahdflkjahldkfhalskjdfhlkjdhflkjhdslfkjadljkfhlakjdflhkdjhflakdjhflakjdshflkjhsdlfkjhalkjdfhlakjhflkjhalsjdhflakjhdfljahsldkjfhalkjdfhlakjhflksdhflkjsdhlfkajlhf"
    solution = sol.buddyStrings(s=s,goal=goal)
    # print(solution)
    assert solution == True
    # print("correct solution")


if __name__ == "__main__":
    cProfile.run('test()', sort='tottime')