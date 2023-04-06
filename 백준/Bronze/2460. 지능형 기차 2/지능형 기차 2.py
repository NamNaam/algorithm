answer = 0
pasg = 0
for i in range(10):
  a, b = map(int, input().split())
  pasg += b - a
  if answer < pasg:
    answer = pasg
print(answer)