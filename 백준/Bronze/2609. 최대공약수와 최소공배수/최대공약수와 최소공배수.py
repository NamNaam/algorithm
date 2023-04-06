a, b = map(int, input().split())
if a > b:
  max = a
else:
  max = b

for i in range(1, max + 1):
  if a % i == 0 and b % i == 0:
    gcd = i
    lcm = i * (a // i) * (b // i)
print(gcd, lcm, sep='\n')