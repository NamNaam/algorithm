from collections import deque

n, m, v = map(int, input().split())
graph = []

# 그래프 초기화
for _ in range(n + 1):
  graph.append([])

# 그래프 생성
for _ in range(m):
  i, j = map(int, input().split())
  graph[i].append(j)
  graph[j].append(i)

# 그래프 정렬
for i in range(n + 1):
  graph[i].sort()

# DFS 함수
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# BFS 함수
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)