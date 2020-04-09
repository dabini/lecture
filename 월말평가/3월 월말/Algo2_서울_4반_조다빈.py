dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def DFS(x, y):
    global cnt

    visited[y][x] = 1

    for d in range(8):
        nx, ny = x+dx[d], y+dy[d]
        if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and arr[ny][nx] == arr[y][x]:
            cnt += 1
            DFS(nx, ny)


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    res = []
    max_w = -1
    res_cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] and not visited[y][x]:
                cnt = 1
                DFS(x, y)
                w = cnt*arr[y][x]
                if max_w < w:
                    max_w = w
                    res_cnt = cnt
                elif max_w == w:
                    if res_cnt > cnt:
                        res_cnt = cnt
    print("#{} {} {}".format(t+1, max_w, res_cnt))


