n = int(input())
num = list(map(int,input().split()))
answer = []

for i in range(n):
  x = num[i]
  answer.insert(i-x, i+1)

print(*answer)