class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        path = []

        def is_palindrome(string):
            left = 0
            right = len(string) - 1

            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1

            return True

        def backtrack(start):
            if start == len(s):
                answer.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return answer