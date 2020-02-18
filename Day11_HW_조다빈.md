# Day 11



### 1. 계산기3

```python
isp = {'(' : 0, '+' : 1, '*' : 2}
icp = {'(' : 3, '+' : 1, '*' : 2}
for t in range(1, 11):
    num = int(input())
    calc = input()
    num_lst = []
    stack = []
    for c in calc:
        if c.isnumeric():
            num_lst += [c]
        elif c == '(':
            stack += [c]
        elif c == ')':
            while stack and stack[-1] != '(':
                p = stack.pop()
                num_lst += [p]
            stack.pop()
        else:
            while stack and isp[stack[-1]] >= icp[c]:
                num_lst += [stack.pop()]
            stack += [c]
    while stack:
        p = stack.pop()
        if p != '(':
            num_lst += [p]

    stack2 = [0]
    for n in num_lst:
        if n.isnumeric():
            stack2 += [int(n)]
        else:
            if n == '+':
                tmp = stack2[-2] + stack2[-1]
            elif n == '*':
                tmp = stack2[-2] * stack2[-1]
            stack2.pop()
            stack2.pop()
            stack2 += [tmp]
    print("#{} {}".format(t, stack2[1]))
```



### 2. 미로

```python
def getSome(x, y):
    global res, maze, visited
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[y][x] = 1
    if maze[y][x] == 3:
        res = 1
        return
    for d in range(4):
        if 0<= x+dx[d] <N and 0<= y+dy[d] <N and maze[y+dy[d]][x+dx[d]] != 1 and not visited[y+dy[d]][x+dx[d]]:
            newx  = x+dx[d]
            newy = y+dy[d]
            getSome(newx, newy)

T = int(input())
for t in range(T):
    res = 0
    N = int(input())
    maze = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for m in range(N):
        maze[m] = list(map(int, input()))

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                startx , starty = x, y
    getSome(startx, starty)
    print("#{} {}".format(t+1, res))
```



### 3. Forth

```python
T = int(input())

for t in range(T):
    code = list(map(str, input().split()))

    stack = []
    temp = 0
    res = ''
    for c in range(len(code)):
        if code[c].isnumeric():
            stack.append(int(code[c]))

        else:
            if code[c] == '.':
                break
            if c == (len(code) -1):
                if code[c] != '.':
                    res = 'error'
            if len(stack) < 2:
                res = 'error'
                break
            if code[c] == "+":
                temp = stack[-2] + stack[-1]
            elif code[c] == '-':
                temp = stack[-2] - stack[-1]
            elif code[c] == '*':
                temp = stack[-2] * stack[-1]
            elif code[c] == '/':
                temp = stack[-2] / stack[-1]
            stack.pop()
            stack.pop()
            stack.append(int(temp))
    if len(stack) > 1:
        res = 'error'
    if res != 'error':
        res = stack[0]
    print("#{} {}".format(t+1, res))
```



### 4. 토너먼트 카드 게임

```python
def rsp(a, b): #1 가위 2 바위 3 보
    if lst[a] == lst[b]:
        return a
    else:
        if lst[a] == 1:
            if lst[b] == 2:
                return b
            elif lst[b] == 3:
                return a
        elif lst[a] == 2:
            if lst[b] == 1:
                return a
            elif lst[b] == 3:
                return b
        else:
            if lst[b] == 1:
                return b
            elif lst[b] == 2:
                return a

def Find(low, high):

    if low == high:
        return low

    else:
        a= Find(low, (low + high) // 2)
        b= Find((low + high) // 2+1, high)

    return rsp(a, b)

T = int(input())
for t in range(T):
    num = int(input())
    lst = [0]
    lst += list(map(int, input().split()))

    print("#{} {}".format(t+1, Find(1, num)))
```



### 5. 배열최소합

```python
T = int(input())

def FindSome(y):
    global N, ans, res
    if y >= N:
        if ans < res:
            res = ans
        return
    for x in range(N):
        if not visited[x] and ans+mymap[y][x] < res:
            visited[x] = 1
            ans += mymap[y][x]
            FindSome(y+1)
            visited[x] =0
            ans -= mymap[y][x]


for t in range(T):
    N = int(input())
    mymap = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    res = 987654321
    ans = 0
    FindSome(0)
    print("#{} {}".format(t+1, res))
```

