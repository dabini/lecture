# 4월 16일 과제

## TREE



### 1. subtree

```python
def check(N):
    global cnt
    if arr[N][0]:
        cnt += 1
        check(arr[N][0])
    if arr[N][1]:
        cnt += 1
        check(arr[N][1])

T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[0]*2 for _ in range(E+2)]
    for i in range(E):
        if not arr[lst[2*i]][0]:
            arr[lst[2*i]][0] = lst[2*i+1]
        else:
            arr[lst[2*i]][1] = lst[2*i+1]
    # print(arr)
    cnt = 1
    check(N)
    print("#{} {}".format(t+1, cnt))
```



### 2. 노드의 합

```python
T= int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    lst = [0] * (N+1)

    for m in range(M):
        nod, num = map(int, input().split())
        lst[nod] = num
    # print(lst)

    if len(lst) % 2:
        lst.append(0)

    for i in range(len(lst)-1, 1, -2):
        lst[i//2] = lst[i] + lst[i-1]


    print("#{} {}".format(t+1, lst[L]))
```

