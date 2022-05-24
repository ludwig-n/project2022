addresses = []
counts = []
for _ in range(int(input())):
    address = input()
    try:
        idx = addresses.index(address)
    except ValueError:
        addresses.append(address)
        counts.append(1)
        print('BMAIL')
    else:
        if counts[idx] == 2:
            print('FAIL')
        else:
            print('BANDEX')
            counts[idx] += 1
