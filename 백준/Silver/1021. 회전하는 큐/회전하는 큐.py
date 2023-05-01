from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

q = deque()
for i in range(1, n+1):
    q.append(i)

for i in arr:
    while True:
        if i == q[0]:
            q.popleft()
            break
        elif q.index(i) <= len(q) // 2:
            q.rotate(-1)
            cnt += 1
        else : # elif i > len(q) / 2:
            q.rotate(1)
            cnt += 1
            
print(cnt)