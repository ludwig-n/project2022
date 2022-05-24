offers = []
for _ in range(int(input())):
    flavor, price = input().split()
    offers.append((flavor, int(price)))

offers.sort()
total = 0
for i, (flavor, price) in enumerate(offers):
    if i == 0 or offers[i - 1][0] != flavor:
        total += price

print(total)
