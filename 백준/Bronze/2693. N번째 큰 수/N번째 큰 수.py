t = int(input())
answer = []

for _ in range(t):
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  answer.append(arr[2])
print(*answer, sep='\n')