class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        answer = 0
        for char in alphabet:
            if char in word and char.upper() in word:
                answer +=1
        return answer
        