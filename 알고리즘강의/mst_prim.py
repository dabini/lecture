"""
input
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

output
[0, 21, 31, 34, 46, 18, 25]
175

"""
import heapq


V, E = map(int, input().split())
adj = {i: [] for i in range(V)}
for i in range(E):
    s, e, c, = map(int, input().split())
    adj[s].append([e, c])
    adj[e].append([s, c])

# 인접리스트 잘 만들어졌는지 확인
# print(adj)

# key, mst, 우선순위 큐 준비
INF = float('inf')
key = [INF] * V
mst = [False] * V
pq = []
result = 0
#시작 정점 선택 : 0
key[0]= 0

#큐에 시작 정점을 넣음 => (key, 정점인덱스)
#우선순위 큐 -> 이진힙 heapq 라이브러리 사용

heapq.heappush(pq, (0,0)) # 우선순위 큐 -> 우선순위: 원소의 첫번째 요소 -> key를 우선순위로

while pq:
    # 최솟값 찾기
    k, node = heapq.heappop(pq)
    if mst[node]:
        continue
    # mst로 선택
    mst[node] = True
    result += k
    # key 갱신 => 키 배열/ 큐
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요 없으면 skip
            heapq.heappush(pq, (key[dest], dest))
print(result)