import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
  q = deque([start])
  visited[start] = True
  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = 0

for _ in range(m): # 그래프 생성
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      visited[i] = True
      cnt += 1
    else:
      bfs(i)
      cnt += 1

print(cnt)