1. Ladder1

```python
for _ in range(10):
    tc = int(input())
    field = [[0]*100 for __ in range(100)]

    for i in range(100):
        field[i] = list(map(int, input().split()))

    for x in range(100):
        if field[99][x] == 2:
            start = x
            break
    a = start
    b = 99

    while True:
        if (a-1) >= 0 and field[b][a-1] == 1:
            while (a-1) >= 0 and field[b][a-1] == 1:
                a -=1
            b -=1
        elif (a+1) <= 99 and field[b][a+1] == 1:
            while (a+1) <= 99 and field[b][a+1] == 1:
                a += 1
            b -= 1
        else:
            b -= 1
        if b == 0:
            break
    print("#{} {}".format(tc, a))
```



2. 파리퇴치

```python
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    field = [[0]*N for _ in range(N)]

    for i in range(N):
        field[i] = list(map(int, input().split()))

    lst = []
    for y in range(N-M+1):
        for x in range(N-M+1):
            cnt = 0
            for z in range(M):
                for v in range(M):
                    cnt += field[y+z][x+v]
            lst += [cnt]
    max_num = max(lst)

    print("#{} {}".format(t+1, max_num))
```

3. 의석이의 세로로말해요

```python
T = int(input())

for t in range(T):
    text = [['*'] * 15 for _ in range(15)]
    word = ""

    for k in range(5):
        w = input()
        for i in range(len(w)):
            text[k][i] = w[i]

    for y in range(15):
        for x in range(15):
            if text[x][y] != '*':
                word += text[x][y]

    print("#{} {}".format(t+1, word))
```