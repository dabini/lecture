# 조다빈_0210



## 1. 괄호검사

```python
T = int(input())

for t in range(T):
    tests = list(map(str, input()))
    stack = [0]
    res = [0] * 128
    res[ord('}')] = '{'
    res[ord(')')] = '('
    for i in range(len(tests)):
        if tests[i] == '{' or tests[i] == '(':
            stack += [tests[i]]
        elif (tests[i] == '}' or tests[i] == ')'):
            stack += [tests[i]]
            if res[ord(tests[i])] == stack[-2]:
                stack.pop()
                stack.pop()

    if stack[-1] == 0:
        ans = 1
    else:
        ans = 0

    print("#{} {}".format(t+1, ans))
```



## 2. 그래프 경로

``` python
def Stack(S):
    global field, G, ans
    visited[S] = 1

    for v in range(1, V+1):
        if field[S][v] == 1 and not visited[v]:
            if v == G:
                ans = 1
                return
            Stack(v)

T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    field = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    ans = 0

    for e in range(E):
        start, end = map(int, input().split())
        field[start][end] = 1
        # indeg[end] += 1
        # outdeg[start] += 1


    S, G = map(int, input().split())
    Stack(S)
    print("#{} {}".format(t+1, ans))
    
```

##  3. 반복문자 지우기

```python
T = int(input())

for t in range(T):
    word = input()
    res = []

    for w in word:
        if w not in res or w != res[-1]:
            res += [w]
        elif w in res and w == res[-1]:
            res.pop()
    print("#{} {}".format(t+1, len(res)))
```