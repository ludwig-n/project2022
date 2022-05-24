actual = list(map(int, input().split()))
predicted = list(map(int, input().split()))
for act1, pred1 in zip(actual, predicted):
    for act2, pred2 in zip(actual, predicted):
        if abs(act1 - pred1) < abs(act2 - pred2):
            break
    else:
        print(abs(act1 - pred1))
        break
