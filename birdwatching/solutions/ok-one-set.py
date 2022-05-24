seen = set()
for _ in range(int(input())):
    genus, spec = input().split()
    if (genus, spec) in seen:
        print('SPECIES')
    else:
        if genus in seen:
            print('GENUS')
        else:
            print('NEW')
            seen.add(genus)
        seen.add((genus, spec))
