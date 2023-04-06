arr = []
for _ in range(9):
  arr.append(int(input()))
sum = sum(arr)

n = sum - 100
breaker = False
for i in range(8):
  for j in range(i+1,9):
    if arr[i] + arr[j] == n:
      a = arr[i]
      b = arr[j]
      arr.remove(a)
      arr.remove(b)
      breaker = True
      break
  if breaker == True:
    break
    
arr.sort()
print(*arr, sep = '\n')
