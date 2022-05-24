s = input()

start = s.find(':')
while start != -1:
    end = s.find(':', start + 1)
    print(s[start + 1:end])
    start = s.find(':', end + 1)
