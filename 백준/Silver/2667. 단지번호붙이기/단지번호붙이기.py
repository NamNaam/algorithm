from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    home_cnt = 1  

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                home_cnt += 1
    return home_cnt

n = int(input())
cnt = 0
ans = []

graph = [list(map(int, input().strip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(graph, i, j))
            cnt += 1

ans.sort()
print(cnt)
for x in ans:
    print(x)