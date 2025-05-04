def mortal_rabbits(n, m):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        if i <= m:
            # последовательность Фибоначчи
            dp[i] = dp[i - 1] + dp[i - 2]
        elif i == m + 1:
            # Первая смерть
            dp[i] = dp[i - 1] + dp[i - 2] - 1
        else:
            # Общ случай с уч смертности
            dp[i] = dp[i - 1] + dp[i - 2] - dp[i - m - 1]

    return dp[n]

n = 6
m = 3
print(mortal_rabbits(n, m))