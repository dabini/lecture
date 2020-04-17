def DFS(x, y):
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    visited[y][x] = 1

    for d in range(8):
        nx, ny = x+dx[d], y+dy[d]
        if 0 <= nx < 10 and 0 <= ny < 10 and arr[ny][nx] and not visited[ny][nx]:
            DFS(nx, ny)

T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(10)]
    visited = [[0]*10 for _ in range(10)]
    cnt = 0

    for y in range(10):
        for x in range(10):
            if arr[y][x] and not visited[y][x]:
                DFS(x, y)
                cnt += 1
    print("#{} {}".format(t+1, cnt))