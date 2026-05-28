from typing import List

class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.best_idx: int = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        def is_better(new_idx: int, old_idx: int) -> bool:
            if old_idx == -1:
                return True

            if len(wordsContainer[new_idx]) < len(wordsContainer[old_idx]):
                return True

            if len(wordsContainer[new_idx]) == len(wordsContainer[old_idx]) and new_idx < old_idx:
                return True

            return False

        root = TrieNode()

        # build reversed trie
        for i, word in enumerate(wordsContainer):
            node = root

            # root = best answer for empty suffix
            if is_better(i, node.best_idx):
                node.best_idx = i

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if is_better(i, node.best_idx):
                    node.best_idx = i

        answer = []
        # Time:  O(C + Q)
        # Space: O(C)
        # C = total number of characters in wordsContainer
        # Q = total number of characters in wordsQuery
        for query in wordsQuery:
            node = root
            answer_idx = root.best_idx

            for ch in reversed(query):
                if ch not in node.children:
                    break

                node = node.children[ch]
                answer_idx = node.best_idx

            answer.append(answer_idx)

        return answer