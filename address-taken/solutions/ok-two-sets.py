bmail = set()
bandex = set()
for _ in range(int(input())):
    address = input()
    if address in bmail:
        if address in bandex:
            print('FAIL')
        else:
            bandex.add(address)
            print('BANDEX')
    else:
        bmail.add(address)
        print('BMAIL')
