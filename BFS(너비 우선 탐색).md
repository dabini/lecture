# BFS(너비 우선 탐색)



### 1. BFS의 특징

- 그래프 탐색 방법

  - DFS(Depth First Search, 깊이 우선 탐색)

    - 스택 활용

  - BFS(Breadth Firsth Search, 너비 우선 탐색)

    - 큐 활용

      시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

      인접한 정점들을 탐색한 후, 차례로 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용

  

![BFS 이미지 검색결과](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FoKP5E%2FbtqxwEjHwHW%2FD6PehDsmMGS2jK5Zkp8rI1%2Fimg.png)



### 2. BFS 알고리즘



- 입력 파라미터: 그래프 G와 탐색 시작점 v

```python
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
```



- 초기상태
  - visited 리스트 초기화
  - Q 생성
  - 시작점 enQueue
- A점부터 시작
  - deQueue A
  - A 방문한 것으로 표시
  - A의 인접점 enQueue
- 탐색 진행
  - deQueue B
  - B 방문한 것으로 표시
  - B의 인접점 enQueue
- 탐색 진행
  - deQueue C
  - C 방문한 것으로 표시
  - C의 인접점 enQueue
- 탐색 진행
  - deQueue D
  - D 방문한 것으로 표시
  - D의 인접점 enQueue
- Q가 비어있으면 탐색 종료