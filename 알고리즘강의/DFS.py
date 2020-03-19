#스택
def DFS(v):
    S = []
    visit = [False] * (V + 1)
    S.append(v)
    visit[v] = True

    while S:
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                S.append(v)
                v = w
                break
            else:
                v = S.pop()
#재귀
def DFS(v):
    visit[v] = True

    for w in G[v]:
        if not visit[w]:
            DFS(w)