k = int(input())
s1 = input()
s2 = input()

if len(s1) >= k and len(s2) >= k and s1[-k:] == s2[-k:]:
    print('YES')
else:
    print('NO')
