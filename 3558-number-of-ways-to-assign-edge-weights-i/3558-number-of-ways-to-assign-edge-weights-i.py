class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Build undirected graph
        graph: dict[int, List[int]] = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        max_depth = 0

        # DFS from root node 1
        # Store current node, parent node, and depth
        stack: List[Tuple[int, int, int]] = [(1, -1, 0)]

        while stack:
            node, parent, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                # Avoid going back to parent
                if nei != parent:
                    stack.append((nei, node, depth + 1))

        return 2**(max_depth -1) % MOD