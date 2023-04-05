t = int(input())
n_list = []

for _ in range(t):
  n = int(input())
  n_list.append(n)

for i in range(len(n_list)):
  n = n_list[i]
  answer = []
  index = 0
  if n == 1:
    print(0)
    continue
  while n // 2 != 1:
    if n % 2 == 1:
      answer.append(index)
      index += 1
      n = n // 2
    else:
      index += 1
      n = n // 2
  if n == 2:
    answer.append(index + 1)
  else:
    answer.append(index)
    answer.append(index + 1)
  print(*answer)