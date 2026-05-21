class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = number of unique BSTs with i nodes
        dp = [0] * (n + 1)

        # Empty tree and single-node tree each have 1 structure
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            total = 0

            # Try each node as the root
            for root in range(1, nodes + 1):
                left_nodes = root - 1
                right_nodes = nodes - root

                total += dp[left_nodes] * dp[right_nodes]

            dp[nodes] = total

        return dp[n]