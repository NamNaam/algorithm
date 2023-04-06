pasg = [list(map(int, input().split())) for _ in range(10)]
out_pasg = 0
in_pasg = 0
answer = 0

for i in range(10):
  in_pasg += pasg[i][1]
  out_pasg += pasg[i][0]
  now_pasg = in_pasg - out_pasg
  if answer < now_pasg:
    answer = now_pasg

print(answer)