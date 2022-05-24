genera = set()
species = set()
for _ in range(int(input())):
    genus, spec = input().split()
    if (genus, spec) in species:
        print('SPECIES')
    else:
        if genus in genera:
            print('GENUS')
        else:
            print('NEW')
            genera.add(genus)
        species.add((genus, spec))
