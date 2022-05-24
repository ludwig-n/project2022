genera = {}
for _ in range(int(input())):
    genus, spec = input().split()
    members = genera.setdefault(genus, set())
    if spec in members:
        print('SPECIES')
    else:
        if members:
            print('GENUS')
        else:
            print('NEW')
        members.add(spec)
