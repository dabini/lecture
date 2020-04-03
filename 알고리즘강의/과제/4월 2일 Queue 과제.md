# 4월 2일 Queue 과제



### 1. 회전

```python
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for m in range(M):
        q = num_lst.pop(0)
        num_lst.append(q)
    print("#{} {}".format(t+1, num_lst[0]))
```



### 2. 피자굽기

```python
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    front = rear = 0
    queue = []
    for n in range(N):
        queue.append([pizza[n], n])

    k = 0
    while len(queue) != 1:
        queue[0][0] //= 2

        if queue[0][0] == 0:
            if N + k < M:
                queue.pop(0)
                queue.append([pizza[N+k], N+k])
                k += 1
            elif N + k >= M:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

    print("#{} {}".format(t+1, queue[0][1] +1))
```