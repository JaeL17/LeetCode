class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_counter: dict[str, List[str]] = dict()
        n = len(strs)
        for i in range(n):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in anagram_counter:
                anagram_counter[sorted_str].append(strs[i])
            else:
                anagram_counter[sorted_str] = [strs[i]]
        return [anagram_counter[key] for key in anagram_counter.keys()]