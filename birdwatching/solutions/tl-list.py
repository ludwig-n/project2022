genera = []
members = []
for _ in range(int(input())):
    genus, spec = input().split()
    try:
        idx = genera.index(genus)
    except ValueError:
        print('NEW')
        genera.append(genus)
        members.append({spec})
    else:
        if spec in members[idx]:
            print('SPECIES')
        else:
            print('GENUS')
            members[idx].add(spec)
