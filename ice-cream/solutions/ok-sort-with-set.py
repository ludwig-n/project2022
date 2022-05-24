offers = []
for _ in range(int(input())):
    flavor, price = input().split()
    offers.append((int(price), flavor))

offers.sort()
flavors = set()
total = 0
for price, flavor in offers:
    if flavor not in flavors:
        flavors.add(flavor)
        total += price

print(total)
