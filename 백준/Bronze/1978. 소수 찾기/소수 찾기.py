n = int(input())
arr = list(map(int, input().split()))
answer = 0

for x in arr:
  dec = True
  if x == 1:
    continue
  mid = x // 2
  if mid <= 1:
    answer += 1
  else:
    for i in range(2, mid+1):
      if x % i == 0:
        dec = False
    if dec == True:
      answer += 1

print(answer)