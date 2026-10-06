class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        top down DP, init 2d array and add 1 for every movement
           0 1 2 3 4 5
        0 [1 1 1 1 1 1]
        1 [1 2 3      ]
        2 [1          ]

        up + left
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[m-1][n-1]