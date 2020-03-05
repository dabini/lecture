import sys
sys.stdin = open('string_input.txt', 'r')


N, K = map(int, input().split())
field = [[0]*(N+1) for _ in range(N+1)]
Visited = [0] *(N+1)
Parent = [0] *(N+1)
res = []
def FindParent(here):
    global res
    res += [here]
    if here == 1:
        return res
    for now in range(N, -1, -1):
        if Parent[here] == now:
            FindParent(now)

def GetSome(here, sofar):
    global ans
    if here == 7:
        if sofar < ans:
            ans = sofar
            return

    for now in range(N+1):
        if field[here][now] and not Visited[now] and sofar + field[here][now] < ans:
            Visited[now] = True
            Parent[now] = here
            GetSome(now, sofar + field[here][now])
            Visited[now] = False

for k in range(K):
    start, end, cost = map(int, input().split())
    field[start][end] = cost
ans = 987654321
GetSome(1, 0)
print(ans)
FindParent(7)
print(*res[::-1])