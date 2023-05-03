from collections import deque

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
distance = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(x1 - 1 , y1 - 1)])

def bfs(x2, y2):
    while q:
        x, y = q.popleft()
        if (x, y) == (x2 - 1, y2 - 1):
            return distance[x2 - 1][y2 - 1]
        for i in range(4):
            for j in range(1, k+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == '#':
                        break
                    if 0 != distance[nx][ny] <= distance[x][y]:
                        break
                    if distance[nx][ny] == 0:
                        distance[nx][ny] = distance[x][y] + 1
                        q.append((nx, ny))
    return -1

print(bfs(x2, y2))