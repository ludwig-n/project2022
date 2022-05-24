import string

def aabaabaa(n):
    if n == 0:
        return ''
    else:
        return aabaabaa(n - 1) + string.ascii_uppercase[n - 1] + \
               aabaabaa(n - 1) + string.ascii_uppercase[n - 1] + aabaabaa(n - 1)

print(aabaabaa(int(input())))
