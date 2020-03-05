Data = list(map(int, input().split()))

def GetSome(depth, r):
    if r == 3:
        for i in range(n):
            if visited[i]:
                print(Data[i], end=" ")
        print()
        return
    if depth >= n:
        return
    visited[depth] = True
    GetSome(depth+1, r+1)
    visited[depth] = False
    GetSome(depth+1, r)

n = 5
r = 3
visited = [0] * n
GetSome(0, 0)