# Day 8 

## 연습문제3_stack

```python
mymap = [[0] * 8 for _ in range(8)]
data = list(map(int, input().split()))
visited = [0] * 8
stack = []
indeg = [0] * 8

def findnext(here):
    for next in range(8):
        if mymap[here][next] and not visited[next]:
            return next


def DFS(here):
    stack.append(here)
    print(here)
    visited[here] = 1

    while stack:
        next = findnext(here)
        while next:
            here = next
            print(here)
            visited[here] = 1
            stack.append(here)
            next = findnext(here)
        here = stack.pop()

howmany = int(len(data)/2)

for i in range(howmany):
    start = data[i*2]
    stop = data[i*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

DFS(1)
```



### 연습문제3_recursion

```python
Data = list(map(int, input().split()))
howmany = len(Data) >> 1
mymap = [[0]*howmany for _ in range(howmany)]
visited = [0] * howmany

def DFS_recursion(here):
    print(here)
    visited[here] = True
    for next in range(howmany):
        if mymap[here][next] and not visited[next]:
            DFS_recursion(next)

for i in range(howmany):
    start = Data[i*2]
    end = Data[i*2+1]
    mymap[start][end] = 1
    mymap[end][start] =1

DFS_recursion(1)
```



### 2.1 AtoI

```python
lst = ['1', '2', '3']
res = 0
for i in range(len(lst)):
    k = ord(lst[i]) - 48
    res += k * 10**(len(lst) - i -1)
print(res)
```



### 2.2 ItoA

```python
i = 123
res = ''
k = 0
check = i

while check > 0 :
    check = check // (10**k)
    k += 1
# print(k) #k=3

for n in range(k):
    a = i % (10** k-n)
res += ascii(a)
print(res)
print(type(res))
```



### 3. GNS

```python
T = int(input())
for _ in range(T):
    t, num = map(str, input().split())
    num = int(num)
    Info = [[[0]*128 for _ in range(128)]for _ in range(128)]
    lst= list(map(str, input().split()))
    cnt = [0] * 10

    Info[ord('Z')][ord('R')][ord('0')] = 0
    Info[ord('O')][ord('N')][ord('E')] = 1
    Info[ord('T')][ord('W')][ord('0')] = 2
    Info[ord('T')][ord('H')][ord('R')] = 3
    Info[ord('F')][ord('O')][ord('R')] = 4
    Info[ord('F')][ord('I')][ord('V')] = 5
    Info[ord('S')][ord('I')][ord('X')] = 6
    Info[ord('S')][ord('V')][ord('N')] = 7
    Info[ord('E')][ord('G')][ord('T')] = 8
    Info[ord('N')][ord('I')][ord('N')] = 9

    for i in range(num):
        cnt[Info[ord(lst[i][0])][ord(lst[i][1])][ord(lst[i][2])]] += 1

    check = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    res = []
    for i in range(10):
        res += [check[i]] * cnt[i]
    res = " ".join(res)

    print("{} {}".format(t, res))
```



### 4. 문자열비교

```python
T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()

    if str1 in str2:
        res = 1
    else:
        res = 0

    print("#{} {}".format(t+1, res))
```

```python
T = int(input())

for t in range(T):
    str1 = input()
    str2 = input()
    res = 0

    for i in range(len(str2)-len(str1)+1):
        check = ''
        for j in range(i, i+len(str1)):
            check += str2[j]
        if check == str1:
            res = 1

    print("#{} {}".format(t+1, res))
```



### 5. 최소 경로

```python
N, K = map(int, input().split())
field = [[0]*(N+1) for _ in range(N+1)]
visited = [0] *(N+1)
stack_lst = []
res = 0

def GetSome(here):
    global res, ans
    if here == 7:
        if res < ans :
            ans=res
            return

    for now in range(N+1):
        if field[here][now] and not visited[now]:
            res += field[here][now]
            visited[now] = 1
            GetSome(now)
            visited[now] = 0
            res -= field[here][now]

for k in range(K):
    start, end, cost = map(int, input().split())
    field[start][end] = cost
ans = 987654321
GetSome(1)
print(ans)
```

