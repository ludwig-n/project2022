s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
else:
    for i, c in enumerate(s1):
        if c.isupper():
            s1 = s1[:i] + c.lower() + s1[i + 1:]
    for i, c in enumerate(s2):
        if c.isupper():
            s2 = s2[:i] + c.lower() + s2[i + 1:]

    if s1 == s2:
        print('YES')
    else:
        print('NO')
