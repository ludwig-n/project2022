k = int(input())
s1 = input()
s2 = input()

if len(s1) < k or len(s2) < k:
    print('NO')
else:
    for i in range(k):
        if s1[-i - 1] != s2[-i - 1]:
            print('NO')
            break
    else:
        print('YES')
