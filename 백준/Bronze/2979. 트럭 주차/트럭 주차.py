a, b, c = map(int, input().split())
cnt = [0]*100
list = []
min = 101
max = 0
ans = 0

for i in range(3):
    n, k = map(int, input().split())
    list.append(n)
    list.append(k)
    for j in range(n, k):
        cnt[j] += 1

for i in list:
    if i <= min:
        min = i
    if i >= max:
        max = i

for i in range(min, max):
    if cnt[i] == 1:
        ans += a
    if cnt[i] == 2:
        ans += 2*b
    if cnt[i] == 3:
        ans += 3*c

print(ans)