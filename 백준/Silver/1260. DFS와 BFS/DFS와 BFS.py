from collections import deque

n, m, v = map(int, input().split())
graph = []
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

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
def dfs(graph, v, visited_dfs):
  visited_dfs[v] = True
  print(v, end = ' ')
  for i in graph[v]:
    if not visited_dfs[i]:
      dfs(graph, i, visited_dfs)

# BFS 함수
def bfs(graph, start, visited_bfs):
  queue = deque([start])
  visited_bfs[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited_bfs[i]:
        queue.append(i)
        visited_bfs[i] = True

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)