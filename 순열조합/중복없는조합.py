Data = [1, 2, 3, 4, 5]

def GetSome(start, r):
    if r == 0:
        print(res)
        return

    for now in range(start, len(Data)):
        if not visited[now] and (now == 0 or Data[now -1] != Data[now] or visited[now-1]):
            visited[now] = True
            res.append(Data[now])
            GetSome(now+1, r-1)
            res.pop()
            visited[now] = False

n = 5
r = 3
res = []
visited = [0] * n
GetSome(0, r)