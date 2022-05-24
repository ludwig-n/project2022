s = input()

in_emoji = False
for char in s:
    if char == ':':
        if in_emoji:
            print()
            in_emoji = False
        else:
            in_emoji = True
    elif in_emoji:
        print(char, end='')
