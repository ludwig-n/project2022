ans = 0
for act, pred in zip(input().split(), input().split()):
    ans = max(ans, abs(int(act) - int(pred)))
print(ans)
