from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] # 상하좌우

t = int(input())

def bfs(graph, i, j):
  queue = deque()
  queue.append((i,j))
  graph[i][j] = 0  

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
  return

for _ in range(t):
  cnt = 0
  n, m, k = map(int, input().split())
  graph = [[0 for _ in range(m)] for _ in range(n)]

  for _ in range(k):
    x, y = map(int, input().split()) # 배추 심어진 위치
    graph[x][y] = 1 # 배추 심기
    
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        bfs(graph, i, j)
        cnt += 1
  print(cnt)