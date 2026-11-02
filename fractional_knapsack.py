
def fractional_knapsack():
    n = int(input("Enter number of items: "))

    items = []

    for i in range(n):
        w, v = map(int, input("Enter weight and value: ").split())
        items.append((w, v, v/w))

    W = int(input("Enter knapsack capacity: "))

    items.sort(key=lambda x: x[2], reverse=True)

    total = 0

    for w, v, r in items:
        if W >= w:
            total += v
            W -= w
        else:
            total += v * (W/w)
            break

    print("Maximum value:", total)


fractional_knapsack()
