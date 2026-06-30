class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            # Expand the window.
            count[s[right]] += 1

            # While the window contains all three characters.
            while count['a'] and count['b'] and count['c']:
                # Every extension to the right is also valid.
                ans += n - right

                # Shrink the window.
                count[s[left]] -= 1
                left += 1

        return ans