m = int(input())
n = int(input())
dec_list = []
sum = 0

for i in range(m, n+1):
  dec = True
  mid = i // 2
  if i == 1:
    continue
  elif i <= 3:
    sum += i
    dec_list.append(i)
    continue
  for j in range(2, mid+1):
    if i % j == 0:
      dec = False
      break
  if dec == True:
    sum += i
    dec_list.append(i)

if len(dec_list) == 0:
  print(-1)
else:
  print(sum)
  print(dec_list[0])