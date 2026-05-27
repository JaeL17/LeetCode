class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}
        
        # time complexity : O(n)
        for i, char in enumerate(word):
            c = char.lower()

            if char.islower():
                last_lower[c] = i
            else:
                if c not in first_upper:
                    first_upper[c] = i

        answer = 0

        for c in last_lower:
            if c in first_upper and last_lower[c] < first_upper[c]:
                answer += 1

        return answer