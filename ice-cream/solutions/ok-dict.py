min_price = {}
for _ in range(int(input())):
    flavor, price = input().split()
    price = int(price)
    cur_price = min_price.setdefault(flavor, price)
    if price < cur_price:
        min_price[flavor] = price

print(sum(min_price.values()))
