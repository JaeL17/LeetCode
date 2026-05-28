from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = TrieNode()

        def is_better(new_idx: int, old_idx: int) -> bool:
            """
            Better means:
            1. shorter word length
            2. if same length, earlier index
            """
            old_idx = root.best_idx if old_idx == -1 else old_idx

            if old_idx == -1:
                return True

            if len(wordsContainer[new_idx]) < len(wordsContainer[old_idx]):
                return True

            if len(wordsContainer[new_idx]) == len(wordsContainer[old_idx]) and new_idx < old_idx:
                return True

            return False

        # Build reversed Trie
        for i, word in enumerate(wordsContainer):

            # root represents empty suffix ""
            if root.best_idx == -1 or is_better(i, root.best_idx):
                root.best_idx = i

            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # this node represents a suffix
                if node.best_idx == -1 or is_better(i, node.best_idx):
                    node.best_idx = i

        answer = []

        # Query
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