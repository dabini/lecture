"""
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력
1 3 7 6 5 2 4
"""
def dfs(v):
    s = []
    visited = [0] * (V+1)
    s.append(v)
    while s:
        u = s.pop()
        if visited[u] == 0:
            print(u, end=" ")
            visited[u] = 1
            for i in range(1, V+1):
                if adj[u][i] == 1 and visited[i] == 0:
                    s.append(i)

V, E = map(int, input().split())
edges = list(map(int, input().split()))

#인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e = edges[2*i], edges[2*i +1]
    adj[s][e] = 1
    adj[e][s] = 1

dfs(1)