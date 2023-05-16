import sys

input = sys.stdin.readline

n = 19

board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, 1, -1] # 하 우 우하 우상
dy = [0, 1, 1, 1]

def omok(x, y):
  color = board[x][y]
  for i in range(4):
    cnt = 1
    nx = x + dx[i]
    ny = y + dy[i]
    while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
      cnt += 1
      if cnt == 5:
        # 육목 판별
        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and board[x - dx[i]][y - dy[i]] == color: 
          break
        if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] == color:
          break
        print(color)
        print(x + 1, y + 1)
        exit(0)
        # return color, x, y
      nx += dx[i]
      ny += dy[i]
      


for x in range(n):
  for y in range(n):
    if board[x][y]:
      omok(x, y)

print(0)