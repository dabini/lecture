### Day7 조다빈 과제



#### 1. 회문

```python
for t in range(10):
    num = int(input())  #회문길이
    field = [[0]*8 for _ in range(8)]

    for k in range(8):
        field[k] = list(map(str, input()))

    res = True
    cnt = 0
    for y in range(8):
        lst = []
        lst2 =[]
        for x in range(8):
            lst += [field[y][x]]
            lst2 += [field[x][y]]

        for n in range(0, (8 - num) +1):
            out = []
            out2 = []
            for m in range(n, n+num):
                out += lst[m]
                out2 += lst2[m]

            if out == out[::-1]:
                cnt += 1

            if out2 == out2[::-1]:
                cnt += 1
    print("#{} {}".format(t+1, cnt))
```



#### 2. 암호생성기

```python
for _ in range(10):
    t = int(input())

    data = list(map(int, input().split()))

    while True:
        if data[-1] == 0:
            break
        for k in range(1, 6):
            if data[0] - k > 0 :
                new = data[0] - k
                data.pop(0)
                data += [new]
            elif data[0] - k <= 0:
                new = 0
                data.pop(0)
                data += [new]
                break
    data = list(map(str, data))
    print("#{} {}".format(t, " ".join(data)))
```

