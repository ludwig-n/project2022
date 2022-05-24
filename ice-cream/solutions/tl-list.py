flavors = []
prices = []
for _ in range(int(input())):
    flavor, price = input().split()
    try:
        idx = flavors.index(flavor)
    except ValueError:
        flavors.append(flavor)
        prices.append(int(price))
    else:
        prices[idx] = min(prices[idx], int(price))

print(sum(prices))
