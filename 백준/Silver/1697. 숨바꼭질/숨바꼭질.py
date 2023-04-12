from collections import deque

def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    x = queue.popleft()
    dx = [-1, 1, x]
    if x == k:
        return visited[x]
    for i in range(3):
      nx = x + dx[i]
      if 0 <= nx < MAX and not visited[nx]:
        visited[nx] = visited[x] + 1
        queue.append(nx)

MAX = 100001
visited = [0]*MAX
n, k = map(int, input().split())

print(bfs())