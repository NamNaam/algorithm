n = int(input())
if n == 0:
  print(0)
else:
  sum = [0]*(n+1)
  sum[0] = 0
  sum[1] = 1
  
  if n >= 2:
    for i in range(2, n+1):
      sum[i] = sum[i-1] + sum[i-2]
      
  print(sum[n])