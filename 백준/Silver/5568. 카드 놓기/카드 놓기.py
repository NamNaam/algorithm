n = int(input())
k = int(input())
card = []
num = []

for _ in range(n):
    card.append(input())

if k == 2:
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            x = card[i]+ card[j]
            if not x in num:
                num.append(x)

elif k == 3:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == i or j == k or k == i:
                    continue
                x = card[i]+ card[j] + card[k]
                if not x in num:
                    num.append(x)

else:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if j == i or j == k or k == i or j == l or k == l or i == l:
                        continue
                    x = card[i]+ card[j] + card[k] + card[l]
                    if not x in num:
                        num.append(x)

print(len(num))