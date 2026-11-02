
def knapsack():
    n = int(input("Enter number of items: "))

    weight = []
    profit = []

    for i in range(n):
        w, p = map(int, input("Enter weight and profit: ").split())
        weight.append(w)
        profit.append(p)

    W = int(input("Enter knapsack capacity: "))

    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weight[i-1] <= w:
                dp[i][w] = max(profit[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("Maximum profit:", dp[n][W])


knapsack()
