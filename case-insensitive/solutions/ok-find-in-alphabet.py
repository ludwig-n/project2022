import string

s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
else:
    for c1, c2 in zip(s1, s2):
        idx1 = string.ascii_uppercase.find(c1)
        if idx1 != -1:
            c1 = string.ascii_lowercase[idx1]
        idx2 = string.ascii_uppercase.find(c2)
        if idx2 != -1:
            c2 = string.ascii_lowercase[idx2]
        if c1 != c2:
            print('NO')
            break
    else:
        print('YES')
