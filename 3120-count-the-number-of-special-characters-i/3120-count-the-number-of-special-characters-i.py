class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        # answer = 0
        # for char in alphabet:
        #     if char in word and char.upper() in word:
        #         answer +=1
        # return answer
        lower = set()
        upper = set()

        # O(n) time complexity 
        for char in word:
            if char.islower():
                lower.add(char)
            else:
                upper.add(char.lower())
        return len(lower & upper)