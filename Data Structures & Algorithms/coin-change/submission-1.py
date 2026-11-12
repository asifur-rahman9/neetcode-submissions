class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        arr = [0] * (amount+1)

        for i in range(1, amount+1):
            mini = float('inf')

            for coin in coins:
                diff = i - coin
                if diff<0:
                    break
                mini = min(mini, arr[diff]+1)

            arr[i] = mini

        if arr[amount] < float('inf'):
            return (arr[amount])
        else:
            return (-1)