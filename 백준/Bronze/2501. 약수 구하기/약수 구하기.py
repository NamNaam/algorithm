n, k = map(int, input().split())
answer_list = []

for i in range(1, n+1):
  if n % i == 0:
    answer_list.append(i)

if len(answer_list) < k:
  answer = 0
else:
  answer = answer_list[k-1]
print(answer)