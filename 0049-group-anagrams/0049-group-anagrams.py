class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_counter: dict[str, List[str]] = dict()
        n = len(strs)

        # n = number of strings in strs
        # k = average length of each string
        # time: O(n * k log k), space: O(n * k)
        for i in range(n):
            sorted_str = ''.join(sorted(strs[i])) # O(k log K) time complexity
            if sorted_str in anagram_counter: # O(1)
                anagram_counter[sorted_str].append(strs[i]) # O(1)
            else:
                anagram_counter[sorted_str] = [strs[i]]
        return [anagram_counter[key] for key in anagram_counter.keys()]