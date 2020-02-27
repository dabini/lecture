def BFS(G, v): #그래프 G, 탐색 시작점 v
    visited = [0]*N #n: 정점의 개수
    queue = [] #큐생성
    queue.append(v) #시작점 v를 큐에 삽입

    while queue:
        t = queue.pop() #큐의 첫번째 원소 반환
        if not visited[t]: #방문하지 않은 곳이면
            visited[t] = True
            visit(t)
        for i in G[t]: #t와 연결된 모든 선에 대해
            if not visited[t]: #방문되지 않은 곳이라면
                queue.append(t)