# 4월 3일 Queue 과제



### 1. 미로의 거리

```python
def bfs(y, x):
    visited[y][x] += 1
    queue.append((y, x))
    global N, res
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        y, x = queue.pop(0)
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<= ny < N and  0<= nx < N:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    queue.append((ny, nx))
                    visited[ny][nx] += 1
                    distance[ny][nx] = distance[y][x] + 1
                    if maze[ny][nx] == 3:
                        res = distance[ny][nx] -1
                        return


T = int(input())
for t in range(T):
    res = 0
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    queue = []
    visited = [[0]*N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]


    for j in range(N):
        for i in range(N):
            if maze[j][i] == 2:
                starty, startx = j, i
    bfs(starty, startx)
    print("#{} {}".format(t+1, res))
```



### 2. 노드의 거리

```python
def BFS(S):
    global check
    q.append(S)
    res.append(S)
    visited[S] = 1
    check = False
    while q:
        n = q.pop(0)
        for new in range(V+1):
            if mymap[n][new] and not visited[new]:
                visited[new] = visited[n] + 1
                q.append(new)
                res.append(new)
T = int(input())

for t in range(T):
    V, E = map(int, input().split()) #V노드의 개수, E 간선 정보
    mymap = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    res = []
    q = []
    for e in range(E):
        start, end = map(int, input().split())
        mymap[start][end] = 1
        mymap[end][start] = 1

    S, G = map(int, input().split())
    BFS(S)
    # print(visited)
    print("#{}".format(t+1), end=" ")
    if visited[G] >0 :
        print(visited[G] -1)
    else:
        print(0)
```