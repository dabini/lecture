## 2월 11일_조다빈 과제 제출



### 1. 농작물관리

```python
T = int(input())

for t in range(T):
    N = int(input())

    field = [[0]*N for _ in range(N)]

    for i in range(N):
        field[i] = list(map(int, input()))

    total = 0
    for y in range(N):
            for x in range(abs(y - N // 2), N-abs(y - N // 2) ):
                total += field[y][x]

    print("#{} {}".format(t+1, total))
```



### 2. 숫자배열회전

```python
T = int(input())

for t in range(T):
    print("#{}".format(t+1))
    N = int(input())

    field = [[0]*N for _ in range(N)]

    for k in range(N):
        field[k] = list(map(str, input().split()))

    out = [[0]*3 for _ in range(N)]

    for y in range(N-1, -1, -1):
        num = ''
        for x in range(N):
            num += field[x][y]
        out[-(y+1)][2] = num


    for y in range(N):
        num = ''
        for x in range(N-1, -1, -1):
            num += field[y][x]
        out[-(y+1)][1] = num

    for y in range(N):
        num = ''
        for x in range(N-1, -1, -1):
            num += field[x][y]
        out[y][0] = num

    for a in range(N):
        print(*out[a])
```



### 3. 자석

```python
def magnetic(lst):
    if lst[-1] == 1:
        lst.pop()
        return magnetic(lst)
    elif lst[0] == 2:
        lst.pop(0)
        return magnetic(lst)

for t in range(10):
    N = int(input())

    table = [[0]*N for _ in range(N)]

    for i in range(N):
        table[i] = list(map(int, input().split()))  #1 = N극 2 = S극

    cnt = 0
    for y in range(N):
        lst = []
        for x in range(N):
            if table[x][y] > 0:
                lst.append(table[x][y])
        magnetic(lst)

        start = 1
        for i in range(1, len(lst)):
            if lst[i-1] ==1 and lst[i] ==2:
                cnt += 1
    print("#{} {}".format(t+1, cnt))
```



### 4.스도쿠검증

```python
T = int(input())

for t in range(10):
    puzzle =[[0]*9 for _ in range(9)]

    for i in range(9):
        puzzle[i] = list(map(int, input().split()))

    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = 1
    for y in range(9):
        empty_y = []
        empty_x = []
        for x in range(9):
            empty_y += [puzzle[y][x]]
            empty_x += [puzzle[x][y]]

        if check != sorted(empty_y):
            res = 0
        if check != sorted(empty_x):
            res = 0

    for y in range(0, 6, 3):
        for x in range(0, 6, 3):
            empty = []
            empty += [puzzle[x][y] , puzzle[x][y+1], puzzle[x][y+2], puzzle[x+1][y] , puzzle[x+1][y+1], puzzle[x+1][y+2],puzzle[x+2][y] , puzzle[x+2][y+1], puzzle[x+2][y+2] ]

            if check != sorted(empty):
                res = 0

    print("#{} {}".format(t+1, res))
```

