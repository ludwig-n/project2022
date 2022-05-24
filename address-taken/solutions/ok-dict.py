address_count = {}
for _ in range(int(input())):
    address = input()
    count = address_count.setdefault(address, 0)
    if count == 2:
        print('FAIL')
    else:
        if count == 1:
            print('BANDEX')
        else:
            print('BMAIL')
        address_count[address] += 1
