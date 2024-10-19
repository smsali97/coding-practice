from typing import List
from collections import defaultdict

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        # Helper function to find all possible ways to build a single layer
        def build_layer(current_width):
            if current_width > width:
                return
            if current_width == width:
                all_layers.append(layer[:])
                return
            for brick in bricks:
                layer.append(brick)
                build_layer(current_width + brick)
                layer.pop()

        # Function to check if two configurations can be placed one over the other
        def is_compatible(layer1, layer2):
            sum1, sum2 = layer1[0], layer2[0]
            index1, index2 = 1, 1
            while index1 < len(layer1) and index2 < len(layer2):
                if sum1 == sum2:
                    return False
                if sum1 < sum2:
                    sum1 += layer1[index1]
                    index1 += 1
                else:
                    sum2 += layer2[index2]
                    index2 += 1
            return True

        mod = 10**9 + 7
        all_layers = []  # To store all possible configurations for one layer
        layer = []  # To store the current layer configuration
        build_layer(0)  # Build layers starting with 0 width

        adjacency_list = defaultdict(list)  # To store the graph of compatible layers
        num_layers = len(all_layers)

        # Build the graph
        for i in range(num_layers):
            if is_compatible(all_layers[i], all_layers[i]):
                adjacency_list[i].append(i)
            for j in range(i + 1, num_layers):
                if is_compatible(all_layers[i], all_layers[j]):
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        # Dynamic programming array initialization
        dp = [[0] * num_layers for _ in range(height)]
        for j in range(num_layers):
            dp[0][j] = 1  # Each configuration is one way to build the first layer

        # Compute number of ways to build the wall using DP
        for i in range(1, height):
            for j in range(num_layers):
                for k in adjacency_list[j]:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod

        return sum(dp[-1]) % mod  # Return the number of ways modulo 10^9 + 7
