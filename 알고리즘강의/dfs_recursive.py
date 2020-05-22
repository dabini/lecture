"""
dfs +재귀
입력
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

출력
1 2 4 6 5 7 3
"""
def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1, V+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)

V, E = map(int, input().split())
edges = list(map(int, input().split()))

#인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    s, e = edges[2*i], edges[2*i +1]
    adj[s][e] = 1
    adj[e][s] = 1

# for row in adj:
#     print(row)

visited = [0] * (V+1)
dfs(1)