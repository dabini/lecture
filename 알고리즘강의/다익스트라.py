"""
다익스트라 + 인접리스트

6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6

"""
# dist, selected 배열 준비
# 시작 정점 선택
# 모든 정점이 선택될 때까지 반복
# 아직 선택되지 않고 dist값이 최소인 정점: u
# 정점 u의 최단거리 결정
# 정점 u에 인접한 정점에 대해서 간선 완화

V, E = map(int, input().split())
adj = {i : [] for i in range(V)}
for i in range(E):
    s, e, c = map(int, input().split())
    # 방향 그래프
    adj[s].append([e, c])

INF = float('inf')
dist = [INF]*V
selected = [False] * V #선택되었는지 안되었는지

dist[0] = 0 #시작점 선택
cnt = 0

while cnt < V:
    #dist가 최소인 정점 찾기
    min = INF
    u = -1
    for i in range(V):
        if not selected[i] and dist[i] < min:
            min = dist[i]
            u = i
    # 결정
    selected[u] = True
    cnt += 1

    # 간선완화
    for w, cost in adj[u]: #도착정점, 가중치
        if dist[w] > dist[u] + cost:
            dist[w] = dist[u] + cost
print(dist)