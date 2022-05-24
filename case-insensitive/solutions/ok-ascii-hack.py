s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
else:
    for c1, c2 in zip(s1, s2):
        if 'A' <= c1 <= 'Z':
            c1 = chr(ord(c1) + 32)
        if 'A' <= c2 <= 'Z':
            c2 = chr(ord(c2) + 32)
        if c1 != c2:
            print('NO')
            break
    else:
        print('YES')
