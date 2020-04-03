#연습문제3
def BFS(n):
    global res
    q.append(n)
    res.append(n)
    visited[n] = 1

    while(q):
        now = q.pop(0)
        for new in range((m+1)):
            if arr[now][new] and not visited[new]:
                q.append(new)
                res.append(new)
                visited[new] = 1

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
m = max(lst)
arr = [[0]* (m+1) for _ in range(m+1)]
q =[]
visited = [0] * (m+1 )
res = []

for i in range(len(lst)//2):
    s = lst[2*i]
    e = lst[(2*i)+1]
    arr[s][e] = 1

BFS(1)
print(res)
