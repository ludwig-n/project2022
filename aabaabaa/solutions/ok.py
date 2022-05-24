import string

def aabaabaa(n):
    if n == 0:
        return ''
    else:
        return '{0}{1}{0}{1}{0}'.format(aabaabaa(n - 1), string.ascii_uppercase[n - 1])

print(aabaabaa(int(input())))
